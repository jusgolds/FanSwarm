from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
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
        return self.abbreviation

class Team(models.Model):
    team_name = models.CharField(max_length=120)
    team_location_name = models.CharField(max_length=120)
    team_metro = models.CharField(max_length=120)
    team_league = models.ForeignKey(League, on_delete=models.CASCADE, default=None)
    team_sport = models.ForeignKey(Sport, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.team_name

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            )

        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=32)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    confirmed = models.BooleanField(default=0)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    user_type = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=70, blank=True)
    user_location = models.CharField(max_length=32, blank=True)
    street_address = models.CharField(max_length=95, blank=True)
    city = models.CharField(max_length=35, blank=True)
    state = models.CharField(max_length=20, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    phone_num = PhoneNumberField(blank=True)
    member_since = models.DateTimeField(auto_now_add=True)
    favorite_teams = models.ManyToManyField(Team, blank=True, related_name='favorite_users')

    USERNAME_FIELD = 'email'
    REQUIREDFIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.username

    def __str__(self):
        return self.name


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    objects = UserManager()

class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    fan_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='+')
    opp_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='+')
    team_league = models.ForeignKey(League, on_delete=models.CASCADE, default=None)
    event_date = models.DateField(default=None)
    event_time = models.TimeField(default=None)
    bar = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='bar')

class EventAttendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    user = models.ManyToManyField(User)
    # fan_group = models.ForeignKey(FanGroup, on_delete=models.CASCADE, blank=True)
