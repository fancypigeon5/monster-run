from . import views
from django.urls import path

urlpatterns = [
    path('battle/', views.battle, name='battle'),
    path('', views.arena, name='arena'),
]