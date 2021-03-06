from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.widgets import Select, SelectMultiple
from django.views.generic.base import TemplateResponseMixin, View

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

    def get_form(self, *args, **kwargs):
        form = super(EventCreateView, self).get_form(*args, **kwargs)
        form.fields['bar'].queryset = User.objects.filter(user_type='bar')
        return form

    def form_valid(self, form):
        event = form.save(commit=False)
        event.owner = User.objects.get(id=self.request.user.pk)
        event.save()
        ea = EventAttendance(event=event)
        ea.save()
        return redirect(self.get_success_url(event_id=event.id))

    def get_success_url(self, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Event successfully added.')
        print(kwargs)
        return reverse('event-detail', kwargs={'event_id':kwargs['event_id']})

class EventListView(ListView):
    template_name = 'events.html'
    model = Event
    slug_field = 'id'
    slug_url_kwarg = 'event_id'
    now = datetime.datetime.now()
    queryset = Event.objects.filter(event_date__gte=now).order_by('event_date')

class EventDetailView(DetailView):
    template_name = 'event_detail.html'
    model = Event
    slug_field = 'id'
    slug_url_kwarg = 'event_id'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        try:
            attendance = EventAttendance.objects.get(event_id=self.object.id)
            context['attendees'] = attendance.user.all()
        except EventAttendance.DoesNotExist:
            pass
        return context

class EventRSVPView(LoginRequiredMixin, TemplateResponseMixin, View):
    http_method_names = ['post']
    model = Event

    def post(self, *args, **kwargs):
        event = self.get_object()
        ea, _ = EventAttendance.objects.get_or_create(event=event)
        ea.user.add(self.request.user)
        ea.save()
        messages.add_message(
            self.request, messages.INFO,
            'You have RSVP\'d to this event.'
        )
        return HttpResponseRedirect(self.get_redirect_url())

    def get_object(self, queryset=None):
        return Event.objects.get(id=self.kwargs['event_id'])

    def get_redirect_url(self, **kwargs):
        return reverse('event-detail', kwargs={'event_id':self.kwargs['event_id']})

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
