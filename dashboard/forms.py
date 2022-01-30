from django import forms
from .models import Message
# from .widgets import RangeInput


class MessageToSelfForm(forms.ModelForm):
    """
    Form for submission of message to self
    """
    class Meta:
        model = Message
        exclude = ('user',) 

    def __init__(self, *args, **kwargs):
        """
        Add placeholde for text box
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'message_text': 'Leave a positive message for your future self!',
        }

        self.fields['message_text'].widget.attrs['placeholder'] = placeholders
        


            

