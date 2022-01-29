from django import forms
from .models import MindfulCheck
from .widgets import RangeInput

class WellnessCheckForm(forms.ModelForm):

    class Meta:
        model = MindfulCheck
        fields = ['purpose', 'emotional', 'financial', 'physical', 'social', 'community', 'career', 'overall']
        widgets = {
            'purpose': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'Purpose','class': 'mindfulScale'}),
            'emotional': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'Emotional','class': 'mindfulScale'}),
            'financial': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'Financial','class': 'mindfulScale'}),
            'physical': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'Physical','class': 'mindfulScale'}),
            'social': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'Social','class': 'mindfulScale'}),
            'community': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'Community','class': 'mindfulScale'}),
            'career': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'Career','class': 'mindfulScale'}),
            'overall': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'Overall','class': 'mindfulScale'}),
        }

    # purpose_range = forms.IntegerField(
    #     widget=RangeInput,
    # )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     mindful_check = MindfulCheck.objects.all()
    #     purpose = [(p.id, p.purpose) for p in mindful_check]



