from . import views
from django.urls import path

urlpatterns = [
    path('<int:equipment_type_id>', views.equipment_create, name='equipment_create'),
    path('', views.equipment, name='equipment'),
]