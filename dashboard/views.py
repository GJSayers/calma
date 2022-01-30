from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings

from .models import UserPreferences, Message
from .forms import UserPreferencesForm

def dashboard(request):
    context = {'form': UserPreferencesForm()}

    return render(request, 'dashboard/index.html', )


def user_prefs(request):
    """
    Display the form for user preference selection / update
    """
    context = {'form': UserPreferencesForm()}

    return render(request, 'dashboard/index.html', context)


def message_self(request):
    """
    Display the form & handle submission for messages to future self
    """
    # if request.user.is_authenticated:
    #     user = UserPreferences.objects.get(user=request.user)
    #     print('user', user)
        # message_form = MessageToSelfForm()
        # message_text = Message.message_text
        # print('message_text', message_text)
        # form_data = {
        #     'user': user,
        #     'message_text': request.POST['message_text']
        # }
        # print('user', user),
        # if request.method == "POST":
        #     print('request post', request.POST)
        #     message_form = MessageToSelfForm(form_data)
        #     print('message_form', user),
        #     if message_form.is_valid():
        #         message_form.save()
            # return redirect(reverse('dashboard/index.html'))   
    # context = {
    #     'message_form': form,
    #     'user': user,
    #     'message_text': message_text,
    # }
    # print('context', context)
    # return render(request, 'dashboard/index.html', context)

# def user_preferences(request):
#     form = UserPreferencesForm()

#     if request.method == 'POST':
#         form = UserPreferencesForm(request.POST)
#         if form.is_valid():
#             form.save()

#     context = {
#         'form': form,
#         # 'user': user,
#         # 'message_text': message_text,
#     }
#     print('context', context)
#     return render(request, 'dashboard/index.html', context)
    

def activities(request):
    """
    Display the video options based on the user preferences, handle the onclick
    """
    return render(request, 'dashboard/index.html')

