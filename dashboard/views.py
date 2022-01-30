from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings

from .models import UserPreferences, MindfulCheck, Message, Activities
from .forms import MessageToSelfForm

def dashboard(request):
    """
    Display the dashboard apps 
    """
    activities = Activities.objects.all()
    print('activities')
    messages = Message.objects.all()
    user = request.user
    print ('requestuser', user)
    form = MessageToSelfForm()
    

    context = {
        'activities': activities,
        'messages': messages,
        'user': user,
        'form': form,
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
    profile = get_object_or_404(Message, user=request.user)
    if request.method == "POST":
        form = MessageToSelfForm(request.POST, instance=profile)
        if form.is_valid():
            form = form.save()
    else: 
        form = MessageToSelfForm(instance=profile)
    form = MessageToSelfForm()

    # context = {'message_text_form': form}
    # template = 'dashboard/index.html'
    return redirect(reverse('dashboard'))

