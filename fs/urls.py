from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('teams/<int:team_id>/', views.TeamDetailView.as_view(), name='team-detail'),
    path('profile/<int:user_id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('events/<int:event_id>/', views.EventDetailView.as_view(), name='event-detail'),
]
