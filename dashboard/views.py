from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings

from .models import UserPreferences, MindfulCheck, Message, Activities
from .forms import MessageToSelfForm, UpdatePreferencesForm 

def dashboard(request):
    """
    Display the dashboard apps 
    """
    activities = Activities.objects.all()
    messages = Message.objects.all()
    user = request.user
    print ('requestuser', user)
    message_form = MessageToSelfForm()
    prefs_form = UpdatePreferencesForm()
        

    context = {
        'activities': activities,
        'messages': messages,
        'user': user,
        'message_form': message_form,
        'prefs_form': prefs_form,
    }

    return render(request, 'dashboard/index.html', context)


def user_prefs(request):
    """
    Handle the message to self submission
    """
    profile = get_object_or_404(Message, user=request.user)
    if request.method == "POST":
        prefs_form = UpdatePreferencesForm(request.POST, instance=profile)
        if prefs_form.is_valid():
            prefs_form = prefs_form.save()
    else: 
        prefs_form = UpdatePreferencesForm(instance=profile)
    prefs_form = UpdatePreferencesForm()

    # context = {'message_text_form': form}
    # template = 'dashboard/index.html'
    return redirect(reverse('dashboard'))


def message_to_self(request):
    """
    Handle the message to self submission
    """
    profile = get_object_or_404(Message, user=request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            message_form = MessageToSelfForm(request.POST, instance=profile)
            if message_form.is_valid():
                message_form = message_form.save()
        else: 
            message_form = MessageToSelfForm(instance=profile)
        message_form = MessageToSelfForm()

        # context = {'message_text_form': form}
        # template = 'dashboard/index.html'
        return redirect(reverse('dashboard'))

