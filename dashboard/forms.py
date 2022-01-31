from django import forms
from .models import Message, UserPreferences, MindfulCheck


class MessageToSelfForm(forms.ModelForm):
    message_text = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Message
        fields = ['message_text']
        