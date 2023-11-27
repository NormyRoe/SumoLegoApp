from datetime import timedelta
from typing import Dict
from urllib import request
from django.test import TestCase
from django.utils import timezone
from drawapp.algorithm import GenerateAllRounds, ValidateRounds
from drawapp.utils import GenerateByeGame, GenerateRoundsForCompetition
from drawapp.views import CreateDrawForCompetition
import legosumodb.models
from django.db.models import Count

# Create your tests here.


def GenerateDummyData(self):
    self.divisionNames = ["Math", "Engineering", "Technology", "Butterflies"]
    self.competitionNames = ["Spring Game", "Summer Game"]
    
    self.school = {}
    self.team = {}
    for schoolNumber in range(1, 5):
        self.school[schoolNumber] = legosumodb.models.School()
        self.school[schoolNumber].name = f"School {schoolNumber}"
        self.school[schoolNumber].street_address_line_1 = ""
        self.school[schoolNumber].street_address_line_2 = ""
        self.school[schoolNumber].suburb = ""
        self.school[schoolNumber].state = ""
        self.school[schoolNumber].postcode = ""
        self.school[schoolNumber].contact_name = ""
        self.school[schoolNumber].contact_number = ""
        self.school[schoolNumber].email_address = ""
        self.school[schoolNumber].paid = True
        self.school[schoolNumber].save()
        
        for divisionName in self.divisionNames:
            teamName = f"Team {divisionName} from School {schoolNumber}"
            self.team[teamName] = legosumodb.models.Team()
            self.team[teamName].name = teamName
            self.team[teamName].school = self.school[schoolNumber]
            self.team[teamName].save()
    
    # Create divisions
    self.division = {}
    for divisionName in self.divisionNames:
        self.division[divisionName] = legosumodb.models.Division()
        self.division[divisionName].name = divisionName
        self.division[divisionName].save()
        
    self.competition = {}
    for competitionName in self.competitionNames:
        self.competition[competitionName] = legosumodb.models.Competition()
        self.competition[competitionName].name = competitionName
        self.competition[competitionName].games_per_team = 4
        self.competition[competitionName].date = timezone.now()
        self.competition[competitionName].save()
        
        # Associate division with competition
        self.divisionhascompetition = {}
        for divisionName in self.divisionNames:
            self.divisionhascompetition[divisionName] = {}
            self.divisionhascompetition[divisionName][competitionName] = legosumodb.models.DivisionHasCompetition()
            self.divisionhascompetition[divisionName][competitionName].competition = self.competition[competitionName]
            self.divisionhascompetition[divisionName][competitionName].division = self.division[divisionName]
            self.divisionhascompetition[divisionName][competitionName].nbr_of_fields = 2
            self.divisionhascompetition[divisionName][competitionName].save()
        
        # Add teams for each school into each division
        oddTeamAdded = False
        for schoolNumber in self.school:
            for divisionName in self.divisionNames:
                teamName = f"Team {divisionName} from School {schoolNumber}"
                division_team = legosumodb.models.DivisionHasTeam()
                division_team.division = self.division[divisionName]
                division_team.team = self.team[teamName]
                division_team.save()

                checked_in = legosumodb.models.CheckedIn()
                checked_in.competition_id = self.competition[competitionName]
                checked_in.division_id = self.division[divisionName]
                checked_in.team_id = self.team[teamName]
                checked_in.checked_in = True
                checked_in.save() 
                
            if not oddTeamAdded:
                oddTeamAdded = True
                teamName = f"Team Odd {divisionName} from School {schoolNumber}"
                
                self.team[teamName] = legosumodb.models.Team()
                self.team[teamName].name = teamName
                self.team[teamName].school = self.school[schoolNumber]
                self.team[teamName].save()
                
                division_team = legosumodb.models.DivisionHasTeam()
                division_team.division = self.division[divisionName]
                division_team.team = self.team[teamName]
                division_team.save()

                checked_in = legosumodb.models.CheckedIn()
                checked_in.competition_id = self.competition[competitionName]
                checked_in.division_id = self.division[divisionName]
                checked_in.team_id = self.team[teamName]
                checked_in.checked_in = True
                checked_in.save() 
                
    # Create fields
    self.fields = {}
    self.divisionFields = {}
    for divisionName in self.divisionNames:
        self.fields[divisionName] = []
        self.divisionFields[divisionName] = []
        
        numberOfFields = list(self.divisionhascompetition[divisionName].values())[0].nbr_of_fields
        for fieldIndex in range(0, numberOfFields):
            # Create field
            field = legosumodb.models.Field()
            field.name = f"Field {fieldIndex+1} for {divisionName}"
            field.save()
            
            # Associate division with field
            divisionField = legosumodb.models.DivisionHasField()
            divisionField.field = field
            divisionField.division = self.division[divisionName]
            divisionField.save()
            
            self.fields[divisionName].append(field)
            self.divisionFields[divisionName].append(divisionField)



class Test(TestCase):
    def setUp(self):
        self.divisionNames = []
        self.competitionNames = []
        self.division : Dict[str, legosumodb.models.Division] = {}
        self.competition : Dict[str, legosumodb.models.Competition] = {}
        self.team : Dict[str, legosumodb.models.Team] = {}
        self.fields = {}
        
        GenerateDummyData(self)
                
    def test_can_retrieve_data(self):
        checkins = legosumodb.models.CheckedIn.objects.all()
        for checkin in checkins:
            print("Found checkin for team `", checkin.team_id.name, "` into competition `", checkin.competition_id.name, "`", sep="")
        self.assertEqual(len(checkins), len(self.team)*len(self.competitionNames))
        

    def test_can_get_teams_checked_into_the_current_competition(self):
        teamsInCurrentCompetition = legosumodb.models.Competition.objects.filter(
            name__contains=self.competitionNames[0],
            checkedin__checked_in=True
        )
        
        # There should be 16 teams
        self.assertEqual(len(teamsInCurrentCompetition), len(self.team))
        
    def test_can_get_count_of_teams_for_each_division_in_current_competition(self):
        startTime = timezone.datetime.now() + timedelta(minutes=5)
        GenerateRoundsForCompetition(self.competition[self.competitionNames[0]], startTime)
        gameResults = list(legosumodb.models.GameResult.objects.all())
        self.assertTrue(len(gameResults) > 0)
        
        for result in gameResults:
            division = result.division
            team_1 = result.team1
            team_2 = result.team2
            gameNumber = result.round
            field = result.field
            gameStartTime = result.start_time
            competition = result.competition
            
            if team_2 != None:
                print(
                    f"Division {division.name}, Competition {competition.name}: Found game for round {gameNumber+1}" + 
                    f" between \"{team_1.name}\" (score: {result.team1_points}) and \"{team_2.name}\" (score: {result.team2_points}) on" +
                    f" field \"{field.name}\" with scheduled at {gameStartTime}"
                )
            else:
                print(
                    f"Division {division.name}, Competition {competition.name}: Found bye for round {gameNumber+1}" + 
                    f" for \"{team_1.name}\" (score: {result.team1_points}) scheduled at {gameStartTime}"
                )
                
    def test_generate_bye_game(self):
        divisionName = self.divisionNames[0]
        division = self.division[divisionName]
        team = list(self.team.values())[0]
        competitionName = self.competitionNames[0]
        competition = self.competition[competitionName]
        time = timezone.datetime.now()
        
        GenerateByeGame(
            division=division,
            competition=competition,
            team_1=team,
            gameNumber=7,
            gameStartTime=time
        )
        
        results = list(legosumodb.models.GameResult.objects.filter(
            division__division_id = division.division_id
        ))
        
        self.assertEqual(len(results),1)
        
        gameResult = results[0]
        self.assertEqual(gameResult.competition.competition_id, competition.competition_id)
        self.assertEqual(gameResult.division.division_id, division.division_id)
        #self.assertTrue((gameResult.start_time - time.time()) )
        self.assertEqual(gameResult.round, 7)
        self.assertEqual(gameResult.team1.team_id, team.team_id)
        self.assertEqual(gameResult.team1_points, 1)
        self.assertEqual(gameResult.team2, None)
        self.assertEqual(gameResult.team2_points, None)
        
        
      
        
    
    
class TestView(TestCase):
    def test_can_call_api_and_get_404_for_non_existant_competition(self):
        apirequest = request.Request("http://localhost", method="POST")
        result = CreateDrawForCompetition(apirequest, 123456789)
        self.assertEqual(result.status_code, 404)
    
    def test_can_call_api_and_get_200_for_known_competition(self):
        GenerateDummyData(self)
        competition = legosumodb.models.Competition.objects.get(
            name=self.competitionNames[0]
        )
        
        apirequest = request.Request("http://localhost", method="POST")
        result = CreateDrawForCompetition(apirequest, competition.competition_id)
        
        self.assertEqual(result.status_code, 200)
        gameResults = list(legosumodb.models.GameResult.objects.all())
        self.assertTrue(len(gameResults) > 0)
    
    
    
    
    
class TestPairingAlgorithm(TestCase):
    def test_can_pair_two_teams(self):
        pairings_all_rounds = GenerateAllRounds(number_of_teams = 2)
        self.assertEqual(len(pairings_all_rounds), 1)
        self.assertTrue(ValidateRounds(pairings_all_rounds))
        
    def test_can_pair_three_teams(self):
        pairings_all_rounds = GenerateAllRounds(number_of_teams = 3)
        self.assertEqual(len(pairings_all_rounds), 3)
        self.assertTrue(ValidateRounds(pairings_all_rounds))
        
    def test_can_pair_four_teams(self):
        pairings_all_rounds = GenerateAllRounds(number_of_teams = 4)
        self.assertEqual(len(pairings_all_rounds), 3)
        self.assertTrue(ValidateRounds(pairings_all_rounds))
        
    def test_can_pair_five_teams(self):
        pairings_all_rounds = GenerateAllRounds(number_of_teams = 5)
        self.assertEqual(len(pairings_all_rounds), 5)
        self.assertTrue(ValidateRounds(pairings_all_rounds))
        
    def test_can_pair_seventeen_teams(self):
        pairings_all_rounds = GenerateAllRounds(number_of_teams = 17)
        self.assertEqual(len(pairings_all_rounds), 17)
        self.assertTrue(ValidateRounds(pairings_all_rounds))
        
    def test_can_pair_eleven_team(self):
        pairings_all_rounds = GenerateAllRounds(number_of_teams =  11)
        self.assertEqual(len(pairings_all_rounds), 11)
        self.assertTrue(ValidateRounds(pairings_all_rounds))
        
