from django import forms
from django.contrib.auth.models import User
from .models import RunData
from equipment.models import Equipment

class UnlockRunDataForm(forms.ModelForm):
    class Meta:
        model = RunData
        fields = ('distance', 'pace', 'equipment', )

class RecoverRunDataForm(forms.ModelForm):
    class Meta:
        model = RunData
        fields = ('distance', 'pace', 'monster', )