from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('teams/', views.TeamListView, name='teams'),
    path('profile/', views.user_display, name='user_display'),
    path('profile/create', views.user_create, name='user_create'),
    path('profile/edit', views.user_edit, name='user_edit'),
    path('events/', views.events, name='events'),
    path('events/create', views.event_create, name='event_create'),
    path('events/edit', views.event_edit, name='event_edit'),
]
