from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import UserPreferences, MindfulCheck, Message
from .forms import WellnessCheckForm


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


    