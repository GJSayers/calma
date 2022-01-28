from django import forms
from checkboxinput import CheckboxInput
from .models import UserPreferences, MindfulCheck


class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        readonly_fields = ('user', 'date')
        widgets = {
            'yoga' : CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            'music' : CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            'mediation' : CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            'puzzles' : CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            'gaming' : CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            'hiit' : CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            'reading' : CheckboxInput(attrs={'class': 'required checkbox form-control'}),

        }

