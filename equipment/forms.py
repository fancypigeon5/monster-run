from django import forms
from .models import Equipment


class EquipForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('monster', )
