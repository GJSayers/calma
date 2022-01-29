from django import forms
from .models import MindfulCheck
from .widgets import RangeInput

class WellnessCheckForm(forms.ModelForm):

    class Meta:
        model = MindfulCheck
        fields = ['purpose', 'emotional', 'financial', 'physical', 'social', 'community', 'career', 'overall']
        widgets = {
            'purpose': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'purposeValue','class': 'mindfulScale'}),
            'emotional': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'emotionalValue','class': 'mindfulScale'}),
            'financial': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'financialValue','class': 'mindfulScale'}),
            'physical': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'physicalValue','class': 'mindfulScale'}),
            'social': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'socialValue','class': 'mindfulScale'}),
            'community': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'communityValue','class': 'mindfulScale'}),
            'career': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'careerValue','class': 'mindfulScale'}),
            'overall': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'id': 'overallValue','class': 'mindfulScale'}),
        }

    # purpose_range = forms.IntegerField(
    #     widget=RangeInput,
    # )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     mindful_check = MindfulCheck.objects.all()
    #     purpose = [(p.id, p.purpose) for p in mindful_check]



