from django.contrib import admin

from .models import Team, League, FanGroup, Sport

admin.site.register(Team)
admin.site.register(League)
admin.site.register(FanGroup)
admin.site.register(Sport)
# Register your models here.
