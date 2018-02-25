from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('teams/<int:team_id>/', views.TeamDetailView.as_view(), name='team-detail'),
    path('profile/<int:user_id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('edit/<int:user_id>/', views.UserEditView.as_view(success_url='thanks'), name='user-edit'),
    path('edit/<int:user_id>/thanks/', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('events/create', views.EventCreateView.as_view(), name='event-create'),
    path('events/<int:event_id>/', views.EventDetailView.as_view(), name='event-detail'),
    path('events/edit/<int:event_id>/', views.EventEditView.as_view(success_url='thanks'), name='event-edit'),
    path('events/edit/<int:event_id>/thanks/', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
]
