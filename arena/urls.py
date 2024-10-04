from . import views
from django.urls import path

urlpatterns = [
    path('battle/', views.battle, name='battle'),
    path('battle/<str:turn>/', views.strike, name='strike'),
    path('lost/', views.lost, name='lost'),
    path('scoreboard/', views.battle, name='scoreboard'),
    path('won/', views.won, name='won'),
    path('', views.arena, name='arena'),
]