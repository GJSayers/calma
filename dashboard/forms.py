from django import forms
from .models import Message, UserPreferences
# from .widgets import RangeInput


class UserPreferencesForm(forms.ModelForm):
    """
    Form for submission of message to self
    """

    WELLNESS_PREFS = (
        ('yoga', 'Yoga'),
        ('meditation', 'Meditation'),
        ('music', 'Music'),
        ('puzzles', 'Puzzles'),
        ('gaming', 'Gaming'),
        ('hiit', 'HIIT'),
        ('reading', 'Reading'),
    )

    # preferences = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices=WELLNESS_PREFS)

    preferences = forms.MultipleChoiceField(choices=WELLNESS_PREFS, widget=forms.RadioSelect(), required=False)

    class Meta:
        model = UserPreferences
        fields = ['preferences']

# class MessageToSelfForm(forms.ModelForm):
    # class Meta:
    #     model = Message
    #     fields = ['message_text']
        # exclude = ('user',) 

    

    # def __init__(self, *args, **kwargs):
    #     """
    #     Add placeholde for text box
    #     """
    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         'message_text': 'Leave a positive message for your future self!',
    #     }

    #     self.fields['message_text'].widget.attrs['placeholder'] = placeholders
