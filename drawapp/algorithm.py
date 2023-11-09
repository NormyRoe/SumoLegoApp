from typing import List, Tuple

def GenerateAllRounds(number_of_teams : int) -> List[List[Tuple[int,int]]]:
    """Generate all pairings for a round robin tournament
    
    To generate a round robin tournament you only need to know the number of teams,
    then you can calculate the games and rounds. 
    
    Algorithm:
    For example we have 5 teams and for round robin only 4 teams can play in a single 
    round and 1 team will have a bye. If we encode the teams by indexes and mark a bye using team -1, then 
    we can select a nominated team which will be always in first pair. 
    
    This is a pattern of 5 teams in a grapg; we have 5 teams and 1 bye(-1):
    
                   2
                  
    1           bye(-1)          3
    
          4              5
          
    The 1-st pair is between middle one and outer one, all other pairs then mirror on the left and right side.
    Round 1:          -1 51234
    -1 and 2
    1 and 3
    5 and 4
    
    Round 2:          -1 12345
    -1 and 3
    2 and 5 
    1 and 4
    
    Round 3:          -1 23451
    -1 and 4
    1 and 5
    2 and 3
    
    Round 4:          -1 34512
    -1 and 5
    4 and 3
    1 and 2
    
    Round 5:          -1 45123
    -1 and 1`
    2 and 4
    3 and 5
    
    

    Args:
        number_of_teams (int): _description_

    Returns:
        List[List[Tuple[int,int]]]: _description_
    """
    teams = list(range(0, number_of_teams))
    pairings_all_rounds = []
    
    if ((number_of_teams % 2) == 1):
        n = (number_of_teams + 1) // 2
        teams.insert(0, -1)
    else:
        n = (number_of_teams) // 2
        
    ## Compute the rounds
    modulo = 2*n - 1
    for i in range(0, 2*n-2 + 1):
        # Pairing is the u node and the i'th v node
        pairings_for_round = []

        ## Inner node to the selected outside node (i)
        team_1 = 0
        team_2 = i + 1
        pairings_for_round.append((teams[team_1], teams[team_2]))
        

        ## Selected outside node (i) to the other outside nodes (k)
        for k in range(1, n):
            # Generate the pairing
            pairing = ((i+k) % modulo, (i-k) % modulo)

            # Sort out the indexes
            team_1 = min(pairing) + 1
            team_2 = max(pairing) + 1
            pairings_for_round.append((teams[team_1], teams[team_2]))
            
        pairings_all_rounds.append(pairings_for_round)
    
    return pairings_all_rounds


def ValidateRounds(pairings_all_rounds : List[List[Tuple[int,int]]]) -> bool:
    number_of_byes = 0
    games_for_team = {}
    
    for pairings_for_round in pairings_all_rounds:
        
        games_for_team_for_round = {}
        for pairing in pairings_for_round:
            
            # The pairing was a bye
            if pairing[0] == -1 or pairing[1] == -1:
                number_of_byes += 1
                continue
            
            # Validate all teams played the same number of games
            games_for_team[pairing[0]] = games_for_team.get(pairing[0], 0) + 1
            games_for_team[pairing[1]] = games_for_team.get(pairing[1], 0) + 1
            
            # A team can only play once in any given round
            games_for_team_for_round[pairing[0]] = games_for_team_for_round.get(pairing[0], 0) + 1
            games_for_team_for_round[pairing[1]] = games_for_team_for_round.get(pairing[1], 0) + 1
            
            # Pairing is invald, the team played itself
            if pairing[0] == pairing[1]:
                return False
        
        # Validate at end of round each team played at most one round
        games_per_team = [games_for_team_for_round[k] for k in games_for_team_for_round.keys()]
        if any([games_played > 1 for games_played in games_per_team]):
            return False
        
    # Validate all teams played the same number of games
    games_per_team = [games_for_team[k] for k in games_for_team.keys()]
    if min(games_per_team) != max(games_per_team):
        return False
    
    # Validate that all teams played as many games as possible
    if min(games_per_team) != (len(games_per_team)-1):
        return False
    
    return True