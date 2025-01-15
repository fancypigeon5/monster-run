from django import forms
from .models import Equipment, EquipmentType


class EquipForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('monster', )


class EquipmentTypeForm(forms.ModelForm):
    class Meta:
        model = EquipmentType
        fields = ('name', 'category', 'benefit_health', 'benefit_damage', 'distance_needed', 'equipment_svg', )