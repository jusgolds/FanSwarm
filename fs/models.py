from django.db import models
import datetime

class Fan_Groups(models.Model):
    group_name = models.CharField(max_length=120)
    official = models.BooleanField(default=0)

class Sports(models.Model):
    BASKETBALL = 'BB'
    BASEBALL = 'BS'
    FOOTBALL = 'FB'
    HOCKEY = 'HY'
    SOCCER = 'SC'
    sport_choices = (
        (BASKETBALL, 'Basketball'),
        (BASEBALL, 'Baseball'),
        (FOOTBALL, 'Football'),
        (HOCKEY, 'Hockey'),
        (SOCCER, 'Soccer'),
    )
    sport_name = models.CharField(max_length=2, choices=sport_choices, default=None)

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

class User_Fan(models.Model):
    username = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=128, default=None)
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=32)
    confirmed = models.BooleanField(default=0)
    member_since = models.DateTimeField(auto_now_add=True)
    fav_nba = models.ForeignKey(Teams, limit_choices_to={'team_league': 1}, on_delete=models.CASCADE, default=None, related_name='+')
    fav_mlb = models.ForeignKey(Teams, limit_choices_to={'team_league': 2}, on_delete=models.CASCADE, default=None, related_name='+')
    fav_nfl = models.ForeignKey(Teams, limit_choices_to={'team_league': 3}, on_delete=models.CASCADE, default=None, related_name='+')
    fav_nhl = models.ForeignKey(Teams, limit_choices_to={'team_league': 4}, on_delete=models.CASCADE, default=None, related_name='+')
    fav_epl = models.ForeignKey(Teams, limit_choices_to={'team_league': 5}, on_delete=models.CASCADE, default=None, related_name='+')
    fav_mls = models.ForeignKey(Teams, limit_choices_to={'team_league': 6}, on_delete=models.CASCADE, default=None, related_name='+')

class User_Bar(models.Model):
    username = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=128, default=None)
    name = models.CharField(max_length=70)
    street_address = models.CharField(max_length=95)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=2, default=None)
    zip_code = models.CharField(max_length=5, default=None)
    phone_num = models.PositiveIntegerField(default=None)
    member_since = models.DateTimeField(auto_now_add=True)
    nba_affiliation = models.ForeignKey(Teams, limit_choices_to={'team_league': 1}, on_delete=models.CASCADE, default=None, related_name='+')
    mlb_affiliation = models.ForeignKey(Teams, limit_choices_to={'team_league': 2}, on_delete=models.CASCADE, default=None, related_name='+')
    nfl_affiliation = models.ForeignKey(Teams, limit_choices_to={'team_league': 3}, on_delete=models.CASCADE, default=None, related_name='+')
    nhl_affiliation = models.ForeignKey(Teams, limit_choices_to={'team_league': 4}, on_delete=models.CASCADE, default=None, related_name='+')
    epl_affiliation = models.ForeignKey(Teams, limit_choices_to={'team_league': 5}, on_delete=models.CASCADE, default=None, related_name='+')
    mls_affiliation = models.ForeignKey(Teams, limit_choices_to={'team_league': 6}, on_delete=models.CASCADE, default=None, related_name='+')

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
    bar = models.ForeignKey(User_Bar, on_delete=models.CASCADE, default=None)
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
    user_role = models.ForeignKey(Attendee_Role, on_delete=models.CASCADE, default=None)
    #need to connect to users
