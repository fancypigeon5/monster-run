from . import views
from django.urls import path

urlpatterns = [
    path('', views.monster, name='home'),
    path('create_monster', views.create_monster, name='create_monster'),
    path('instructions', views.instructions, name='instructions'),
]
