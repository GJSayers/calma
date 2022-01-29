from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import UserPreferences, MindfulCheck, Message


def user_prefs(request):
    """
    Display the u
    """
    return render(request, 'dashboard/index.html')


def message_self(request):
    """
    Display the dashboard apps with the logged 
    """
    return render(request, 'dashboard/index.html')

