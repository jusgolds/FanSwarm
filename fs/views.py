from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from .models import Team, User, Event

class TeamListView(ListView):
    template_name = 'teams.html'
    model = Team

class TeamDetailView(DetailView):
    model = Team
    slug_field = 'id'
    slug_url_kwarg = 'team_id'

class UserEditView(UpdateView):
    model = User
    fields = ['email', 'user_location']
    template_name = 'user_edit.html'
    success_field = '/thanks/'
    slug_field = 'id'
    slug_url_kwarg = 'user_id'

class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = User
    slug_field = 'id'
    slug_url_kwarg = 'user_id'

class EventCreateView(CreateView):
    model = Event
    fields = ['fan_team', 'opp_team', 'event_date', 'event_time']
    template_name = 'create_event.html'

class EventListView(ListView):
    template_name = 'events.html'
    model = Event
    slug_field = 'id'
    slug_url_kwarg = 'event_id'

class EventDetailView(DetailView):
    model = Event
    slug_field = 'id'
    slug_url_kwarg = 'event_id'

class EventEditView(UpdateView):
    model = Event
    fields = ['event_date', 'event_time', 'fan_team', 'opp_team']
    template_name = 'event_edit.html'
    success_field = '/thanks/'
    slug_field = 'id'
    slug_url_kwarg = 'event_id'

def thanks(request):
    return HttpResponse("Thanks!")

def login(request):
    return HttpResponse("This is where someone would login.")
