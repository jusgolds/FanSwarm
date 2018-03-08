from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages

from .models import Team, User, Event, League
from .forms import UserEditForm, EventCreateForm, EventEditForm, TeamEditForm

import datetime

class TeamListView(ListView):
    template_name = 'teams.html'
    model = Team

class TeamDetailView(DetailView):
    model = Team
    slug_field = 'id'
    slug_url_kwarg = 'team_id'

class UserEditView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'user_edit.html'
    slug_field = 'id'
    slug_url_kwarg = 'user_id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Profile successfully updated.')
        return reverse_lazy('user-detail', kwargs={'user_id':self.kwargs['user_id']})


class TeamEditView(UpdateView):
    model = User
    form_class = TeamEditForm
    template_name = 'favorite_team_edit.html'
    slug_field = 'id'
    slug_url_kwarg = 'user_id'

    def get_form(self, *args, **kwargs):
        form = super(TeamEditView, self).get_form(*args, **kwargs)
        form.fields['favorite_teams'].queryset = Team.objects.filter(team_league=1)
        return form

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Teams successfully updated.')
        return reverse_lazy('user-detail', kwargs={'user_id':self.kwargs['user_id']})


class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = User
    slug_field = 'id'
    slug_url_kwarg = 'user_id'

class EventCreateView(CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'create_event.html'
    success_url = reverse_lazy('events')

    def get_form(self, *args, **kwargs):
        form = super(EventCreateView, self).get_form(*args, **kwargs)
        form.fields['bar'].queryset = User.objects.filter(user_type='bar')
        return form

class EventListView(ListView):
    template_name = 'events.html'
    model = Event
    slug_field = 'id'
    slug_url_kwarg = 'event_id'
    now = datetime.datetime.now()
    queryset = Event.objects.filter(event_date__gte=now).order_by('event_date')

class EventDetailView(DetailView):
    model = Event
    slug_field = 'id'
    slug_url_kwarg = 'event_id'

class EventEditView(UpdateView):
    model = Event
    form_class = EventEditForm
    template_name = 'event_edit.html'
    slug_field = 'id'
    slug_url_kwarg = 'event_id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Profile successfully updated.')
        return reverse_lazy('event-detail', kwargs={'event_id':self.kwargs['event_id']})

def thanks(request):
    return HttpResponse("Thanks!")

def login(request):
    return HttpResponse("This is where someone would login.")
