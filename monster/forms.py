from django import forms
from .models import Monster

class MonsterForm(forms.ModelForm):
    color=forms.CharField(max_length=7,widget=forms.TextInput(attrs={"type": "color", }))
    class Meta:
        model = Monster
        fields = ('name', 'type', 'color', )
