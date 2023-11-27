from datetime import timedelta
from django.utils import timezone
from typing import Dict, List, Tuple
from drawapp.algorithm import GenerateAllRounds
from legosumodb.models import Division, Competition, Team, DivisionHasCompetition, Field, GameResult
from django.db.models import Count
import logging


def GetCompetitionForCompetitionId(competition_id : int) -> Competition:
    """Get Competition object for given ID

    If the Competition is not found Competition.DoesNotExist is raised

    Args:
        competition_id (int): The Competition ID to be found

    Returns:
        Competition: The Competition object
    """
    competition = Competition.objects.get(
        competition_id = competition_id
    )
    
    return competition


def GetDivisionsForCompetitionWithTeamCountAnnotation(competition : Competition) -> List[Division]:
    """Get Divisions For Competition With Team Count Annotation
    
    The division object will have an additional property, num_teams which is the
    count of distinct checkins for the competition. Note that we
    use distinct to avoid double counting a single team.

    Args:
        competition (Competition): Competition to get divisions for

    Returns:
        List[Division]: All divisions in competition with num_teams attribute
    """
    divisionsForCurrentCompetitionWithTeamCount = Division.objects.filter(
        checkedin__competition_id__competition_id=competition.competition_id,
        checkedin__checked_in=True,
    ).annotate(num_teams=Count("checkedin__team_id", distinct=True))
    
    return list(divisionsForCurrentCompetitionWithTeamCount)


def GetNumberOfFieldsForDivisionCompetition(division : Division, competition : Competition) -> int:
    """Get Number Of Fields For Division-Competition

    The division can have an arbitary number of fields, but there is an additional
    constraint regarding how many fields can actually be used for the given competition.

    A competition can reuse the same divisions so we need to know both the
    division and competition.

    Args:
        division (Division): Division to get the number of fields for
        competition (Competition): The competition for the given division

    Returns:
        int: Number of fields
    """
    divisionHasCompetitionInformation = list(DivisionHasCompetition.objects.filter(
        competition__competition_id = competition.competition_id,
        division__division_id = division.division_id
    ))
    
    return divisionHasCompetitionInformation[0].nbr_of_fields


def GetFieldsForDivision(division : Division) -> List[Field]:
    """Get Fields for Division

    Args:
        division (Division): Division to get the fields for

    Returns:
        List[Field]: All fields for the given division
    """
    fieldsForDivisionInformation = list(Field.objects.filter(
        divisionhasfield__division__division_id=division.division_id    
    ))
    return fieldsForDivisionInformation


def GetTeamsPlayingInDivisionCompetition(division : Division, competition : Competition) -> List[Team]:
    """Get Teams Playing In Division-Competition

    Args:
        division (Division): Division to get the teams for
        competition (Competition): The competition to get the teams for

    Returns:
        List[Team]: Teams in the Division-Competition
    """
    teamsPlayingInDivisionForCompetition = list(Team.objects.filter(
        checkedin__checked_in=True,
        checkedin__competition_id__competition_id = competition.competition_id,
        checkedin__division_id__division_id = division.division_id
    ))
    
    return teamsPlayingInDivisionForCompetition


def GenerateRoundsForCompetition(competition : Competition, startTime : timezone.datetime, options : Dict[str, str] = {}):
    """_summary_

    Args:
        competition (Competition): Competition to generate rounds for
        startTime (timezone.datetime): Start time of the competition
        options (Dict[str, str], optional): Any options to change the match making. Defaults to {}.
    """
    
    # Need to get divisions for competition and will add the team count
    divisionsForCurrentCompetitionWithTeamCount = GetDivisionsForCompetitionWithTeamCountAnnotation(competition)
    
    # Generate all pairings   
    for division in divisionsForCurrentCompetitionWithTeamCount:
        GenerateRoundsForDivision(division, competition, startTime, options)


def GenerateRoundsForDivision(division : Division, competition : Competition, startTime : timezone.datetime, options : Dict[str, str] = {}):
    """_summary_

    Args:
        division (Division): Division to generate rounds for
        competition (Competition): Competition to generate rounds for
        startTime (timezone.datetime): Start time of the competition
        options (Dict[str, str], optional): Any options to change the match making. Defaults to {}.
    """
    # Calculate pairing
    pairings_all_rounds = GenerateAllRounds(number_of_teams = division.num_teams)
    
    # Get number of fields from division information
    numberOfFieldsToUse = GetNumberOfFieldsForDivisionCompetition(division, competition)
    
    # Get fields for division
    fields = GetFieldsForDivision(division)
    
    # There must be enough fields
    if not(numberOfFieldsToUse <= len(fields)):
        raise RuntimeError(f"Competition (\"{competition.name}\") expected at least {numberOfFieldsToUse} field(s) to be assigned to Division (\"{division.name}\") but got {len(fields)}")
    
    # Get actual teams
    teams = GetTeamsPlayingInDivisionCompetition(division, competition)
    
    GenerateGamesForDivision(division, competition, pairings_all_rounds, numberOfFieldsToUse, fields, teams, startTime, options)
   
    
def GenerateGamesForDivision(division : Division,
                             competition : Competition,
                             pairings_all_rounds : List[List[Tuple[int, int]]],
                             numberOfFieldsToUse : int,
                             fields : List[Field],
                             teams : List[Team],
                             startTime : timezone.datetime,
                             options : Dict[str, str] = {}):
    """_summary_

    Args:
        division (Division): Division to generate games for
        competition (Competition): Competition to generate games for
        pairings_all_rounds (List[List[Tuple[int, int]]]): All the parings
        numberOfFieldsToUse (int): Number of fields to use
        fields (List[Field]): All the fields that are available
        teams (List[Team]): All teams that will play
        startTime (timezone.datetime): Start time of the first game
        options (Dict[str, str], optional): Any options to change the match making. Defaults to {}.
    """
    # Load configuration options
    CONFIG_REPEAT_GAMES_WHEN_MORE_GAMES_REQUESTED = options.get("CONFIG_REPEAT_GAMES_WHEN_MORE_GAMES_REQUESTED", True)
    CONFIG_MINUTES_PER_GAME = options.get("CONFIG_MINUTES_PER_GAME", 5)
    CONFIG_MINUTES_BETWEEN_GAMES_ON_SAME_FIELD = options.get("CONFIG_MINUTES_BETWEEN_GAMES_ON_SAME_FIELD", 0)
    
    for gameNumber in range(0, competition.games_per_team):
        roundRobinIndex = gameNumber % len(pairings_all_rounds)
        pairing_for_round = pairings_all_rounds[roundRobinIndex]
        
        # Check if we are needing to generate more rounds than round robin pairs
        if gameNumber >= len(pairings_all_rounds):
            if not CONFIG_REPEAT_GAMES_WHEN_MORE_GAMES_REQUESTED:
                logging.debug(f"All rounds complete, but more games requested. Config is to not repeat games. Stopping.")
                break
            logging.debug(f"All rounds complete, but more games requested. Config is to repeat games. Repeating round {roundRobinIndex+1}")
        
        number_of_field_allocations = 0
        for pairing in pairing_for_round:
            # Calculate the schedule offset
            # 9:10                  9:15                 9:15                  9:20                  9:20
            # x<-- play 5 minutes -->x<-- teams change -->x<-- play 5 minutes -->x<-- teams change -->x<-- play 5 minutes -->x
            # r<-- ROUND 1                                                    -->x<-- ROUND 2
            scheduleOffset = number_of_field_allocations // numberOfFieldsToUse
            scheduleOffsetMinutes = (gameNumber + scheduleOffset)*(CONFIG_MINUTES_PER_GAME + CONFIG_MINUTES_BETWEEN_GAMES_ON_SAME_FIELD)
            gameStartTime = startTime + timedelta(minutes=scheduleOffsetMinutes)
            
            if min(pairing) == -1:
                # Get the team
                team_1 = teams[max(pairing)]
                
                # Genearte bye game
                GenerateByeGame(division, competition, team_1, gameNumber + 1, gameStartTime)
                
            else:
                # Get the teams
                team_1 = teams[pairing[0]]
                team_2 = teams[pairing[1]]
                
                # Get the field (also note the field allocation)
                selected_field = number_of_field_allocations % numberOfFieldsToUse
                field = fields[selected_field]
                number_of_field_allocations += 1
            
                # Generate standard game                
                GenerateStandardGame(division, competition, gameNumber + 1, gameStartTime, field, team_1, team_2)
                

def GenerateStandardGame(division : Division, competition : Competition, gameNumber : int, gameStartTime : timezone.datetime, field : Field, team_1 : Team, team_2 : Team):
    """_summary_

    Args:
        division (Division): Division for the game
        competition (Competition): Competition for the game
        gameNumber (int): Round or Game number
        gameStartTime (timezone.datetime): When the game will start
        field (Field): Field for the game
        team_1 (Team): First Team for the game
        team_2 (Team): Second Team for the game
    """
    logging.debug(f"Division {division.name}: Adding game for round {gameNumber+1}" + 
                              f" between \"{team_1.name}\" and \"{team_2.name}\" on" +
                              f" field \"{field.name}\" with scheduled at {gameStartTime}")
    
    gameResult = GameResult()
    gameResult.team1 = team_1
    gameResult.team2 = team_2
    gameResult.round = gameNumber
    gameResult.team1_points = 0
    gameResult.team2_points = 0
    gameResult.field = field
    gameResult.start_time = gameStartTime
    gameResult.division = division
    gameResult.competition = competition
    gameResult.save()
                

def GenerateByeGame(division : Division, competition : Competition, team_1 : Team, gameNumber : int, gameStartTime : timezone.datetime):
    """_summary_

    Args:
        division (Division): Division for the game
        competition (Competition): Competition for the game
        team_1 (Team): Team for the game
        gameNumber (int): Round or Game number
        gameStartTime (timezone.datetime): When the game will start
    """
    logging.debug(f"Division {division.name}: for game {gameNumber+1} team {team_1.name} will have a bye")
                
    gameResult = GameResult()
    gameResult.team1 = team_1
    gameResult.round = gameNumber
    gameResult.team1_points = 1
    gameResult.start_time = gameStartTime
    gameResult.division = division
    gameResult.competition = competition
    gameResult.save()