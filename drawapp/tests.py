from django.test import TestCase
from django.utils import timezone
from drawapp.algorithm import GenerateAllRounds, ValidateRounds
import legosumodb.models

# Create your tests here.


class Test(TestCase):
    def setUp(self):
        # data required to make a draw
        self.competition = legosumodb.models.Competition()
        self.competition.name = "game"
        self.competition.games_per_team = 4
        self.competition.date = timezone.now()
        self.competition.save()
        
        self.division = legosumodb.models.Division()
        self.division.name = "division"
        self.division.save()
        
        self.divisionhascompetition1 = legosumodb.models.DivisionHasCompetition()
        self.divisionhascompetition1.competition = self.competition
        self.divisionhascompetition1.division = self.division
        self.divisionhascompetition1.nbr_of_fields = 4
        self.divisionhascompetition1.save()
        
        self.school = legosumodb.models.School()
        self.school.name = "School 1"
        self.school.street_address_line_1 = ""
        self.school.street_address_line_2 = ""
        self.school.suburb = ""
        self.school.state = ""
        self.school.postcode = ""
        self.school.contact_name = ""
        self.school.contact_number = ""
        self.school.email_address = ""
        self.school.paid = True
        self.school.save()
        
        for team_number in range(1, 9):
            self.team = legosumodb.models.Team()
            self.team.name = "Team "+str(team_number)
            self.team.school = self.school
            self.team.save()

            self.checked_in = legosumodb.models.CheckedIn()
            self.checked_in.competition_id = self.competition
            self.checked_in.division_id = self.division
            self.checked_in.team_id = self.team
            self.checked_in.checked_in = True
            self.checked_in.save() 
                
    def test_can_retrieve_data(self):
        """
        check that we can get data from the database
        """
        checkins = legosumodb.models.CheckedIn.objects.all()
        self.assertEqual(len(checkins), 8)
        for checkin in checkins:
            print("Found checkin for team `", checkin.team_id.name, "` into competition `", checkin.competition_id.name, "`", sep="")
    
    
    def test_create_draw(self):
        team_1 = legosumodb.models.Team.objects.get(name = "Team 1")
        self.assertEqual(team_1.school.name, "School 1")
    

class TestPairingAlgorithm(TestCase):
    def test_can_pair_two_teams(self):
        #
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
        
    def test_can_pair_twelve_teams(self):
        pairings_all_rounds = GenerateAllRounds(number_of_teams = 12)
        self.assertEqual(len(pairings_all_rounds), 11)
        self.assertTrue(ValidateRounds(pairings_all_rounds))
        
    def test_can_pair_seventeen_teams(self):
        pairings_all_rounds = GenerateAllRounds(number_of_teams = 17)
        self.assertEqual(len(pairings_all_rounds), 17)
        self.assertTrue(ValidateRounds(pairings_all_rounds))
        
