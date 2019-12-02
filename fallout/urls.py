# coding: utf-8
from django.urls import path

from fallout import views


namespace = 'fallout'
app_name = 'fallout'
urlpatterns = [
    path('', views.view_index, name='index'),
    path('token/<str:token>/', views.view_token, name='token'),
    path('campaign/<int:campaign_id>/dashboard/', views.view_dashboard, name='dashboard'),
    path('campaign/<int:campaign_id>/', views.view_campaign, name='campaign'),
    path('character/<int:character_id>/', views.view_character, name='character'),
    path('next_turn/<int:campaign_id>/', views.next_turn, name='next_turn'),
    path('simulation/', views.simulation, name='simulation'),
    path('thumbnails/', views.thumbnails, name='thumbnails'),
]
