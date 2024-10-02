from . import views
from django.urls import path

urlpatterns = [
    path('select/<int:equipment_type_id>', views.equipment_create, name='equipment_create'),
    path('equip/<int:equipment_id>', views.equip_to, name='equip_to'),
    path('unequip/<int:equipment_id>', views.unequip, name='unequip'),
    path('unlock/<int:equipment_id>', views.unlock, name='unlock'),
    path('', views.equipment, name='equipment'),
]