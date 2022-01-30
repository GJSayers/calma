from django import forms
from django.forms import MultipleChoiceField, CheckboxSelectMultiple
# from multiselectfield import CheckboxSelectMultiple
from .models import Message, UserPreferences, MindfulCheck



class MessageToSelfForm(forms.ModelForm):
    message_text = forms.CharField(max_length=255, required=False)

    class Meta:
        model = UserPreferences
        fields = ['message_text']


class UpdatePreferencesForm(forms.ModelForm):
    WELLNESS_PREFS = [
        ('yoga', 'Yoga'),
        ('meditation', 'Meditation'),
        ('music', 'Music'),
        ('puzzles', 'Puzzles'),
        ('gaming', 'Gaming'),
        ('hiit', 'HIIT'),
        ('reading', 'Reading'),
    ]
    preferences = MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=WELLNESS_PREFS)

    class Meta:
        model = UserPreferences
        fields = ['preferences']
        