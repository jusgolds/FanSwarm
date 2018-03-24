from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms.widgets import Select, SelectMultiple

from .models import Team, User, Event, League
from .forms import UserEditForm, EventCreateForm, EventEditForm, TeamEditForm, FavoriteTeamForm

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
        #if statement: teaeam.id is in favorite_teams don't do anything, if it isn't there add it
        form = self.get_form()
        if not form.is_valid():
            error_string = 'Bad data, check the form'
            return HttpResponse(error_string, status=400)
        user = User.objects.filter(pk=self.object.pk).update(**params)
        return redirect(self.get_success_url())
        #return render(self.request, self.template_name, context)

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
        form = super(UserEditView, self).get_form(*args, **kwargs)
        form.fields['leagues'].widget = Select(choices=League.objects.only('league_name', 'pk'))
        form.fields['favorite_teams'].queryset = Team.objects.filter('leagues')
        return form

    def post(self, request, *args, **kwargs):
        params = dict(request.POST.items())
        # print the params, find your form in the data
        print(params)
        form = params.get('UserEditForm')
        if not form.is_valid():
            error_string = 'Bad data, check the form'
            return HttpResponse(error_string, status=400)
        # print out the form, find the field
        # probably called 'id_league' or similar
        print(form.items())
        # delete the league field
        form.pop('league_name')
        favorite = form.save()
        return render(self.request, self.template_name, context)

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
