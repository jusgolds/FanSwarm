from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('profile/', views.user_display, name='user_display'),
    path('profile/create', views.user_create, name='user_create'),
    path('profile/edit', views.user_edit, name='user_edit'),
    path('events/', views.events, name='events'),
    path('events/create', views.event_create, name='event_create'),
    path('events/edit', views.event_edit, name='event_edit'),
]
