from django import forms
from .models import Message
# from .widgets import RangeInput


class MessageToSelfForm(forms.ModelForm):
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

    preferences = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices=WELLNESS_PREFS)

    class Meta:
        model = Message
        fields = ['preferences']
        # exclude = ('user',) 

    

    def __init__(self, *args, **kwargs):
        """
        Add placeholde for text box
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'message_text': 'Leave a positive message for your future self!',
        }

        self.fields['message_text'].widget.attrs['placeholder'] = placeholders
        


            

