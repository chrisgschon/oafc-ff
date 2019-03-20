from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.player_list, name='player_list'),
    path('players/<int:pk>/', views.player_details, name='player_details'),
]