from django.db import models

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
    state = models.CharField(max_length=2, default=None)
    zip_code = models.CharField(max_length=5, default=None)
    phone_num = models.PositiveIntegerField(default=None)
    #need to add password, member_since, avatar, teams

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

class Fan_Groups(models.Model):
    group_name = models.CharField(max_length=120)
    official = models.BooleanField(default=0)

class Events(models.Model):
    bar = models.ForeignKey(User_Bar, on_delete=models.CASCADE, default=None)
    group = models.ForeignKey(Fan_Groups, on_delete=models.CASCADE, default=None)
