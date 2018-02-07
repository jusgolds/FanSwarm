from django.db import models

class Leagues(models.Model):
    league_name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=32)
    BASKETBALL = 'BB'
    FOOTBALL = 'FB'
    BASEBALL = 'BS'
    HOCKEY = 'HY'
    SOCCER = 'SC'
    sport_choices = (
        (BASKETBALL, 'Basketball'),
        (FOOTBALL, 'Football'),
        (BASEBALL, 'Baseball'),
        (HOCKEY, 'Hockey'),
        (SOCCER, 'Soccer'),
    )
    sport = models.CharField(max_length=2, choices=sport_choices, default=None)

class Teams(models.Model):
    team_name = models.CharField(max_length=120)
    team_location_name = models.CharField(max_length=120)
    team_metro = models.CharField(max_length=120)
    team_league = models.ForeignKey(Leagues, on_delete=models.CASCADE, default=None)
    #need to add fan_group

class User_Fan(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=32)
    #need to add password, member since, avatar, confirmed, fav teams

class User_Bar(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=70)
    street_address = models.CharField(max_length=95)
    city = models.CharField(max_length=35)
    #need to add password, state, zip, phone_num, member_since, avatar, teams
