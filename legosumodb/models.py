# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Competition(models.Model):
    competition_id = models.AutoField(db_column='Competition_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    games_per_team = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Competition'


class Division(models.Model):
    division_id = models.AutoField(db_column='Division_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Division'


class School(models.Model):
    school_id = models.AutoField(db_column='School_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    street_address_line_1 = models.CharField(max_length=45, blank=True, null=True)
    street_address_line_2 = models.CharField(max_length=45, blank=True, null=True)
    suburb = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    postcode = models.CharField(max_length=4, blank=True, null=True)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email_address = models.CharField(max_length=60, blank=True, null=True)
    paid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'School'


class User(models.Model):
    user_id = models.AutoField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=45, blank=True, null=True)
    surname = models.CharField(max_length=45, blank=True, null=True)
    email_address = models.CharField(max_length=60, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    role = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Field(models.Model):
    field_id = models.AutoField(db_column='Field_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    judge = models.ForeignKey('User', models.DO_NOTHING, db_column='judge', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field'


class Team(models.Model):
    team_id = models.AutoField(db_column='Team_id', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey(School, models.DO_NOTHING, db_column='School_id')  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Team'


class DivisionHasCompetition(models.Model):
    divisionhascompetition_id = models.AutoField(db_column='DivisionhasCompetition_id', primary_key=True)  # Field name made lowercase.
    division = models.ForeignKey(Division, models.DO_NOTHING, db_column='Division_id')  # Field name made lowercase.
    competition = models.ForeignKey(Competition, models.DO_NOTHING, db_column='Competition_id')  # Field name made lowercase.
    nbr_of_fields = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Division_has_Competition'
        unique_together = (('division_id', 'competition_id'),)


class DivisionHasField(models.Model):
    divisionhasfield_id = models.AutoField(db_column='DivisionhasField_id', primary_key=True)  # Field name made lowercase.
    division = models.ForeignKey(Division, models.DO_NOTHING, db_column='Division_id')  # Field name made lowercase.
    field = models.ForeignKey('Field', models.DO_NOTHING, db_column='Field_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Division_has_Field'
        unique_together = (('division_id', 'field_id'),)


class DivisionHasTeam(models.Model):
    divisionhasteam_id = models.AutoField(db_column='DivisionhasTeam_id', primary_key=True)  # Field name made lowercase.
    division = models.ForeignKey(Division, models.DO_NOTHING, db_column='Division_id')  # Field name made lowercase.
    team = models.ForeignKey('Team', models.DO_NOTHING, db_column='Team_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Division_has_Team'
        unique_together = (('division_id', 'team_id'),)


class CheckedIn(models.Model):
    checked_in_id = models.AutoField(db_column='Checked_In_id', primary_key=True)  # Field name made lowercase.
    competition_id = models.ForeignKey('Competition', models.DO_NOTHING, db_column='Competition_id')  # Field name made lowercase.
    division_id = models.ForeignKey('Division', models.DO_NOTHING, db_column='Division_id')  # Field name made lowercase.
    team_id = models.ForeignKey('Team', models.DO_NOTHING, db_column='Team_id')  # Field name made lowercase.
    checked_in = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Checked_In'
        unique_together = (('team_id', 'division_id', 'competition_id'),)


class GameResult(models.Model):
    game_id = models.AutoField(db_column='Game_id', primary_key=True)  # Field name made lowercase.
    competition_id = models.ForeignKey(Competition, models.DO_NOTHING, db_column='Competition_id')  # Field name made lowercase.
    division_id = models.ForeignKey(Division, models.DO_NOTHING, db_column='Division_id')  # Field name made lowercase.
    round = models.IntegerField(blank=True, null=True)
    team1 = models.ForeignKey('Team', models.DO_NOTHING, db_column='team1', blank=True, null=True)
    team2 = models.ForeignKey('Team', models.DO_NOTHING, db_column='team2', related_name='gameresult_team2_set', blank=True, null=True)
    field = models.ForeignKey(Field, models.DO_NOTHING, db_column='field', blank=True, null=True)
    team1_points = models.IntegerField(blank=True, null=True)
    team2_points = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Game_Result'
        unique_together = (('game_id', 'division_id', 'competition_id'),)








