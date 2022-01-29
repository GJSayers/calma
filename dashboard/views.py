from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import UserPreferences, MindfulCheck, Message


def dashboard(request):
    """
    Display the dashboard apps with the logged 
    """
    mindful_checks = MindfulCheck.objects.all()

    form = WellnessCheckForm()

    if request.method == "POST":
        print(request.POST)
        form = WellnessCheckForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {
        'form': form,
        'mindful_checks': mindful_checks,
    }
    
    return render(request, 'dashboard/index.html', context)


def user_prefs(request):
    """
    Display the form for user preference selection / update
    """
    return render(request, 'dashboard/index.html')


def message_self(request):
    """
    Display the form & handle submission for messages to future self
    """
    return render(request, 'dashboard/index.html')

def activities(request):
    """
    Display the video options based on the user preferences, handle the onclick
    """
    return render(request, 'dashboard/index.html')

