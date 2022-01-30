from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import UserPreferences, MindfulCheck, Message, Activities

def dashboard(request):
    """
    Display the dashboard apps 
    """
    activities = Activities.objects.all()
    print('activities')
    messages = Message.objects.all()
    user = request.user
    print ('requestuser', user)
    

    context = {
        'activities': activities,
        'messages': messages,
        'user': user,
    }

    return render(request, 'dashboard/index.html', context)


# def user_prefs(request):
#     """
#     Display the u
#     """
#     return render(request, 'dashboard/index.html')


def message_to_self(request):
    """
    Handle the message to self submission
    """
    user = request.user


    return redirect(reverse, 'dashboard/index.html')

