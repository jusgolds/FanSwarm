from django.contrib import admin

from .models import Team, League, FanGroup, Sport, User, Event

admin.site.register(Team)
admin.site.register(League)
admin.site.register(FanGroup)
admin.site.register(Sport)
admin.site.register(User)
admin.site.register(Event)
# Register your models here.
