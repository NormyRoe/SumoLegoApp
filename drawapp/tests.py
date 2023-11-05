from django.test import TestCase
from django.utils import timezone
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
        self.divisionhascompetition1.nbr_of_fields = 1
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
        
        self.team1 = legosumodb.models.Team()
        self.team1.name = "Team 1"
        self.team1.school = self.school
        self.team1.save()

        self.checked_in1 = legosumodb.models.CheckedIn()
        self.checked_in1.competition_id = self.competition
        self.checked_in1.division_id = self.division
        self.checked_in1.team_id = self.team1
        self.checked_in1.checked_in = True
        self.checked_in1.save() 
                
    def test_can_retrieve_data(self):
        """
        check that we can get data from the database
        """
        checkins = legosumodb.models.CheckedIn.objects.all()
        self.assertEqual(len(checkins), 1)
        for checkin in checkins:
            print("Found checkin for team `", checkin.team_id.name, "` into competition `", checkin.competition_id.name, "`", sep="")
    
    