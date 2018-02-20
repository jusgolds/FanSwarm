from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Team, User, Event

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

class EventListView(ListView):
    template_name = 'events.html'
    model = Event

class EventDetailView(DetailView):
    model = Event
    slug_field = 'id'
    slug_url_kwarg = 'event_id'

def login(request):
    return HttpResponse("This is where someone would login.")
