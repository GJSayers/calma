from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User

from .models import UserPreferences, Message
from .forms import MessageToSelfForm


def user_prefs(request):
    """
    Display the form for user preference selection / update
    """
    return render(request, 'dashboard/index.html')


def message_self(request):
    """
    Display the form & handle submission for messages to future self
    """
    user = session.user
    message_form = MessageToSelfForm()
    if request.method == "POST":
        print(request.POST)
        message_form = MessageToSelfForm(request.POST)
        if message_form.is_valid():
            message_form.save()
        return redirect(reverse('dashboard/index.html'))   
    context = {
        'message_form': message_form,
        'user': User,
    }
    return render(request, 'dashboard/index.html', context)
    

def activities(request):
    """
    Display the video options based on the user preferences, handle the onclick
    """
    return render(request, 'dashboard/index.html')

