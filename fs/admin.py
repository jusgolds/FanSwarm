from django.contrib import admin

from .models import Team, League, FanGroup, Sport, User

admin.site.register(Team)
admin.site.register(League)
admin.site.register(FanGroup)
admin.site.register(Sport)
admin.site.register(User)
# Register your models here.
