from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms.widgets import Select, SelectMultiple

from .models import Team, User, Event, EventAttendance, League
from .forms import UserEditForm, EventCreateForm, EventEditForm

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

    def get_form(self, *args, **kwargs):
        form = super(UserEditView, self).get_form(*args, **kwargs)
        form.fields['leagues'].queryset = League.objects.all()
        form.fields['favorite_teams'].queryset = Team.objects.all()
        return form

    def post(self, request, *args, **kwargs):
        print(request.POST)
        self.object = self.get_object()
        context = super(UserEditView, self).get_context_data(**kwargs)
        teamids = request.POST.getlist('favorite_teams')
        params = dict(request.POST.items())
        params.pop('leagues')
        params.pop('csrfmiddlewaretoken')
        params.pop('favorite_teams')
        fteams = User.objects.get(pk=self.object.pk).favorite_teams.all()
        print(fteams)
        ftids = [f.id for f in fteams]
        removed = [f for f in fteams if f not in teamids]
        User.objects.get(pk=self.object.pk).favorite_teams.remove(*removed)
        for t in teamids:
            if t in ftids:
                continue
            else:
                User.objects.get(pk=self.object.pk).favorite_teams.add(t)
        form = self.get_form()
        if not form.is_valid():
            error_string = 'Bad data, check the form'
            return HttpResponse(error_string, status=400)
        user = User.objects.filter(pk=self.object.pk).update(**params)
        return redirect(self.get_success_url())

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Profile successfully updated.')
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

class EventRSVPDetailView(DetailView):
    template_name = 'event_rsvp.html'
    model = EventAttendance
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
