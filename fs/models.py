from django.db import models
import datetime

class FanGroup(models.Model):
    group_name = models.CharField(max_length=120)
    official = models.BooleanField(default=0)

class Sport(models.Model):
    sport_name = models.CharField(max_length=32, default=None)

    def __str__(self):
        return self.sport_name

class League(models.Model):
    league_name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=32)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.league_name

class Team(models.Model):
    team_name = models.CharField(max_length=120)
    team_location_name = models.CharField(max_length=120)
    team_metro = models.CharField(max_length=120)
    team_league = models.ForeignKey(League, on_delete=models.CASCADE, default=None)
    team_sport = models.ForeignKey(Sport, on_delete=models.CASCADE, default=None)
    fan_group = models.ForeignKey(FanGroup, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.team_name

class User(models.Model):
    username = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=128, default=None)
    confirmed = models.BooleanField(default=0)
    user_type = models.CharField(max_length=32, default=None)
    name = models.CharField(max_length=70)
    user_location = models.CharField(max_length=32)
    street_address = models.CharField(max_length=95)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=5)
    phone_num = models.PositiveIntegerField(default=None)
    member_since = models.DateTimeField(auto_now_add=True)

class FavoriteTeam(models.Model):
    user_id = models.ManyToManyField(User)
    fav_team = models.ManyToManyField(Team)

class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    fan_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='+')
    opp_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='+')
    event_date = models.DateField(default=None)
    event_time = models.TimeField(default=None)
    bar = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='bar')
    group = models.ForeignKey(FanGroup, on_delete=models.CASCADE, default=None)

class EventAttendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    user = models.ManyToManyField(User)
