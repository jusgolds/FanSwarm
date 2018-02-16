from django.db import models
import datetime

class Fan_Groups(models.Model):
    group_name = models.CharField(max_length=120)
    official = models.BooleanField(default=0)

class Sports(models.Model):
    sport_name = models.CharField(max_length=32, default=None)

class Leagues(models.Model):
    league_name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=32)
    sport = models.ForeignKey(Sports, on_delete=models.CASCADE, default=None)

class Teams(models.Model):
    team_name = models.CharField(max_length=120)
    team_location_name = models.CharField(max_length=120)
    team_metro = models.CharField(max_length=120)
    team_league = models.ForeignKey(Leagues, on_delete=models.CASCADE, default=None)
    team_sport = models.ForeignKey(Sports, on_delete=models.CASCADE, default=None)
    fan_group = models.ForeignKey(Fan_Groups, on_delete=models.CASCADE, default=None)

class User(models.Model):
    username = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=128, default=None)
    name = models.CharField(max_length=70)
    user_location = models.CharField(max_length=32)
    street_address = models.CharField(max_length=95)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=5)
    phone_num = models.PositiveIntegerField(default=None)
    member_since = models.DateTimeField(auto_now_add=True)
    
class Favorite_Teams(models.Model):
    user_id = models.ManyToManyField(User)
    fav_team = models.ManyToManyField(Teams)

class Bar_Role(models.Model):
    USER_CREATED = 'UC'
    BAR_CREATED = 'BC'
    GROUP_SPONSORED = 'GS'
    role_choices = (
        (USER_CREATED, 'User Created'),
        (BAR_CREATED, 'Bar Created'),
        (GROUP_SPONSORED, 'Group Sponsored'),
    )
    role_name = models.CharField(max_length=2, choices=role_choices, default=USER_CREATED)

class Events(models.Model):
    fan_team = models.ForeignKey(Teams, on_delete=models.CASCADE, default=None, related_name='+')
    opp_team = models.ForeignKey(Teams, on_delete=models.CASCADE, default=None, related_name='+')
    event_date = models.DateField(default=None)
    event_time = models.TimeField(default=None)
    bar = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    bar_role = models.ForeignKey(Bar_Role, on_delete=models.CASCADE, default=None)
    group = models.ForeignKey(Fan_Groups, on_delete=models.CASCADE, default=None)


class Attendee_Role(models.Model):
        ORGANIZER = 'OG'
        ATTENDEE = 'AT'
        role_choices = (
            (ORGANIZER, 'Organizer'),
            (ATTENDEE, 'Attendee'),
        )
        role_name = models.CharField(max_length=2, choices=role_choices, default=ORGANIZER)

class Event_Attendence(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, default=None)
    user = models.ManyToManyField(User)
    user_role = models.ForeignKey(Attendee_Role, on_delete=models.CASCADE, default=None)
