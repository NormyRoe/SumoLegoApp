# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CheckedIn(models.Model):
    team_id = models.OneToOneField('Team', models.DO_NOTHING, db_column='Team_id', primary_key=True)  # Field name made lowercase. The composite primary key (Team_id, Division_id, Competition_id) found, that is not supported. The first column is selected.
    division_id = models.ForeignKey('DivisionHasCompetition', models.DO_NOTHING, db_column='Division_id')  # Field name made lowercase.
    competition_id = models.ForeignKey('DivisionHasCompetition', models.DO_NOTHING, db_column='Competition_id', related_name='checkedin_competition_set')  # Field name made lowercase.
    checked_in = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Checked_In'
        unique_together = (('team_id', 'division_id', 'competition_id'),)


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
    nbr_of_fields = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Division'


class DivisionHasCompetition(models.Model):
    Division_id = models.OneToOneField(Division, models.DO_NOTHING, db_column='Division_id', primary_key=True)  # Field name made lowercase. The composite primary key (Division_id, Competition_id) found, that is not supported. The first column is selected.
    Competition_id = models.ForeignKey(Competition, models.DO_NOTHING, db_column='Competition_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Division_has_Competition'
        unique_together = (('Division_id', 'Competition_id'),)


class DivisionHasField(models.Model):
    division = models.OneToOneField(Division, models.DO_NOTHING, db_column='Division_id', primary_key=True)  # Field name made lowercase. The composite primary key (Division_id, Field_id) found, that is not supported. The first column is selected.
    field = models.ForeignKey('Field', models.DO_NOTHING, db_column='Field_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Division_has_Field'
        unique_together = (('division', 'field'),)


class DivisionHasTeam(models.Model):
    division = models.OneToOneField(Division, models.DO_NOTHING, db_column='Division_id', primary_key=True)  # Field name made lowercase. The composite primary key (Division_id, Team_id) found, that is not supported. The first column is selected.
    team = models.ForeignKey('Team', models.DO_NOTHING, db_column='Team_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Division_has_Team'
        unique_together = (('division', 'team'),)


class Field(models.Model):
    field_id = models.AutoField(db_column='Field_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    judge = models.ForeignKey('User', models.DO_NOTHING, db_column='judge', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Field'


class GameResult(models.Model):
    game_id = models.AutoField(db_column='Game_id', primary_key=True)  # Field name made lowercase. The composite primary key (Game_id, Division_id, Competition_id) found, that is not supported. The first column is selected.
    round = models.IntegerField(blank=True, null=True)
    team1 = models.ForeignKey('Team', models.DO_NOTHING, db_column='team1', blank=True, null=True)
    team2 = models.ForeignKey('Team', models.DO_NOTHING, db_column='team2', related_name='gameresult_team2_set', blank=True, null=True)
    field = models.ForeignKey(Field, models.DO_NOTHING, db_column='field', blank=True, null=True)
    team1_points = models.IntegerField(blank=True, null=True)
    team2_points = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    division = models.ForeignKey(DivisionHasCompetition, models.DO_NOTHING, db_column='Division_id')  # Field name made lowercase.
    competition = models.ForeignKey(DivisionHasCompetition, models.DO_NOTHING, db_column='Competition_id', related_name='gameresult_competition_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Game_Result'
        unique_together = (('game_id', 'division', 'competition'),)


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


class Team(models.Model):
    team_id = models.AutoField(db_column='Team_id', primary_key=True)  # Field name made lowercase.
    school = models.ForeignKey(School, models.DO_NOTHING, db_column='School_id')  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Team'


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


class Mytest(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mytest'
