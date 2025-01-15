from . import views
from django.urls import path

urlpatterns = [
    path('select/<int:equipment_type_id>',
         views.equipment_create, name='equipment_create'),
    path('equip/<int:equipment_id>', views.equip_to, name='equip_to'),
    path('unequip/<int:equipment_id>', views.unequip, name='unequip'),
    path('unlock/<int:equipment_id>', views.unlock, name='unlock'),
    path('add_equipment_type', views.add_equipment_type, name='add_equipment_type'),
    path('edit_or_delete_type', views.edit_or_delete_type, name='edit_or_delete_type'),
    path('edit_equipment_type/<int:equipment_type_id>', views.edit_equipment_type, name='edit_equipment_type'),
    path('delete_equipment_type/<int:equipment_type_id>', views.delete_equipment_type, name='delete_equipment_type'),
    path('', views.equipment, name='equipment'),
]
