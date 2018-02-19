from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Team, User

class TeamListView(ListView):
    template_name = 'teams.html'
    model = Team

class TeamDetailView(DetailView):
    model = Team
    slug_field = 'id'
    slug_url_kwarg = 'team_id'

class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = User
    slug_field = 'id'
    slug_url_kwarg = 'user_id'

def login(request):
    return HttpResponse("This is where someone would login.")

def user_create(request):
    return HttpResponse("This is where a user would create their profile.")

def user_edit(request):
    return HttpResponse("This is where a user would edit their profile.")

def user_display(request):
    return HttpResponse("This is where a user would view their profile.")

def events(request):
    return HttpResponse("This is where a user can view all of the events.")

def event_create(request):
    return HttpResponse("This is where a user would create an event.")

def event_edit(request):
    return HttpResponse("This is where a user would edit an event.")

def event_display(request):
    return HttpResponse("This is where a user would view the event")
