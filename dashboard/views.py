from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
import json

from .models import UserPreferences, MindfulCheck, Message
from .forms import WellnessCheckForm


def dashboard(request):
    """
    Display the dashboard apps with the logged 
    """

    return render(request, 'dashboard/index.html', )

def mindful_check(request):
    mindful_checks = MindfulCheck.objects.all()

    form = WellnessCheckForm()

    profile = get_object_or_404(MindfulCheck, user=request.user)

    if request.method == "POST":
        print(request.POST)
        form = WellnessCheckForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = WellnessCheckForm(instance=profile)
    form = WellnessCheckForm()
            
    context = {
        'data': {
            'model': serializers.serialize('json', MindfulCheck.objects.all()),
        },
        'form': form,
        'mindful_checks': mindful_checks,
    }

    return render(request, 'dashboard/mindful_check.html', context)
    
def mindful_results(request):
    pass