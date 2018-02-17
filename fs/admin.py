from django.contrib import admin

from .models import Teams, Leagues, Fan_Groups, Sports

admin.site.register(Teams)
admin.site.register(Leagues)
admin.site.register(Fan_Groups)
admin.site.register(Sports)
# Register your models here.
