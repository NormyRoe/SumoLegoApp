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
    pivot -> center
    non-pivot -> non-center
    
                   2
                  
    1           bye(-1)          3
    
          5              4
          
    The 1-st pair is between middle one and outer one, all other pairs then mirror on the left and right side.
                       ----------
    Round 1:          -1   5 1 |2| 3 4
                             -------
                           -----------
    -1 and 2
    1 and 3
    5 and 4
    
                       ----------
    Round 2:          -1   1 2 |3| 4 5
                             -------
                           -----------
    -1 and 3
    2 and 4 
    1 and 5
    
                       ----------
    Round 3:          -1   2 3 |4| 5 1
                             -------
                           -----------
    -1 and 4
    3 and 5
    2 and 1
    
                       ----------
    Round 4:          -1   3 4 |5| 1 2
                             -------
                           -----------
    -1 and 5
    4 and 1
    3 and 2
    
                       ----------
    Round 5:          -1   4 5 |1| 2 3
                             -------
                           -----------
    -1 and 1`
    5 and 2
    4 and 3
    
    

    Args:
        number_of_teams (int): _description_

    Returns:
        List[List[Tuple[int,int]]]: list of all rounds containing a list of all pairs 
    """
    teams = list(range(0, number_of_teams))
    pairings_all_rounds = []
    
    # algorithm value n is the number of teams divided by 2
    half_number_of_teams = (number_of_teams) // 2
    
    # when the numbre of teams is odd:
    if ((number_of_teams % 2) == 1):
        half_number_of_teams = (number_of_teams + 1) // 2
        # insert bye team on the [0] position
        teams.insert(0, -1)
        
    # Compute the rounds
    number_of_nonpivot_teams = 2*half_number_of_teams - 1
    for pivot_index in range(0, number_of_nonpivot_teams):
        # Pairing is the pivot node and the corresponding non_pivot node
        pairings_for_round = []

        # Pivot node to the selected outside node (non-pivot node)
        # team_1 is always a pivote node
        team_1 = 0
        team_2 = pivot_index + 1
        pairings_for_round.append((teams[team_1], teams[team_2]))
        

        # Selected non pivot node to the other non pivot nodes
        # pivot_index_offset = > when me moving left and ringht from the pivot index
        # 1 represents 1 step away from pivot index (bye -> 2) so it is 1 and 3
        # half_number_of_teams is 3 and it represent that we can do one more step from pivot_index
        for pivot_index_offset in range(1, half_number_of_teams):
            # Generate the pairing
            non_pivot_pairing_indexes = (
                (pivot_index+pivot_index_offset) % number_of_nonpivot_teams,
                (pivot_index-pivot_index_offset) % number_of_nonpivot_teams
            )

            # Do all pivot pairing
            # team 1 has the lower index than team2
            # we are addding 1 because we need to add pivot
            
            
            # original array is P:
            # index 0  1  2  3  4  5
            # P =  [A, B, C, D, E, F]
            
            # V = [A] ---> pivot
            
            # index 0  1  2  3  4 
            # U =  [B, C, D, E, F] ---> non-pivot
            # to go from U to P we need to add 1 to an index
            team_1 = min(non_pivot_pairing_indexes) + 1
            team_2 = max(non_pivot_pairing_indexes) + 1
            # create a list of teams in tuple of (team_1, team_2) ---> per single round
            pairings_for_round.append((teams[team_1], teams[team_2]))
        
        # add all team pairings for a singe round to the list of all rounds ---> all rounds
        pairings_all_rounds.append(pairings_for_round)
    
    return pairings_all_rounds


 
    #                2
    
                  
                  
    # 1           bye(-1)          3
    
    
    
    #       5              4

# check if the algorithm is correct
def ValidateRounds(pairings_all_rounds : List[List[Tuple[int,int]]]) -> bool:
    number_of_byes = 0
    games_for_team = {}
    
    for pairings_for_round in pairings_all_rounds:
        
        teams_who_have_played_this_round = {}
        for pairing in pairings_for_round:
            team_1 = pairing[0]
            team_2 = pairing[1]
            
            # Pairing is invald, the team played itself
            if team_1 == team_2:
                return False
            
            # The pairing was a bye
            if team_1 == -1 or team_2 == -1:
                number_of_byes += 1
                continue
            
            # A team should appear only once per round
            if team_1 in teams_who_have_played_this_round or team_2 in teams_who_have_played_this_round:
                return False
            
            # Note who has played in the round
            teams_who_have_played_this_round[team_1] = True
            teams_who_have_played_this_round[team_2] = True
            
            # Sum all games a team has played in all rounds
            games_for_team[team_1] = games_for_team.get(team_1, 0) + 1
            games_for_team[team_2] = games_for_team.get(team_2, 0) + 1
        
    # Validate all teams played the same number of games
    games_per_team = list(games_for_team.values()) # [games_for_team[team_name] for team_name in games_for_team.keys()]
    if min(games_per_team) != max(games_per_team):
        return False
    
    # Validate that all teams played as many games as possible
    if min(games_per_team) != (len(games_per_team)-1):
        return False
    
    return True