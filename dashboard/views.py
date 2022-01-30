from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings

from .models import UserPreferences, Message
from .forms import UserPreferencesForm, MessageToSelfForm

def dashboard(request):
    

    context = {'form': UserPreferencesForm()}

    return render(request, 'dashboard/index.html', context)


# def user_prefs(request):
#     """
#     Display the form for user preference selection / update
#     """
#     context = {'form': UserPreferencesForm()}

#     return render(request, 'dashboard/index.html', context)
    

def message_self_content(request):
    # Show individual news messages
    
    messages = Message.objects.all()


    context = {
        'messages': messages,
    }

    return render(request, 'dashboard/message_self_content.html', context)

def add_message_self(request):
    """
    Display the form & handle submission for messages to future self
    """
# if request.user.is_authenticated:
    #     user = Message.objects.get(user=request.user)
    #     print('user', user)
    # message_form = MessageToSelfForm()
    # message_text = Message.message_text
    # print('message_text', message_text)
    # form_data = {
    #     # 'user': user,
    #     'message_text': request.POST.get('message_text')
    # }
    # # print('user', user),
    # if request.method == "POST":
    #     print('request post', request.POST)
    #     message_form = MessageToSelfForm(form_data)
        # print('message_form', user),
        # if message_form.is_valid():
        #     msg = message_form.save(commit=False)
        #     msg.user = request.user
        #     msg.save()
    profile = get_object_or_404(Message, user=request.user)

    if request.method == "POST":
        form = MessageToSelfForm(request.POST, instance=profile)
        # form = Message(request.POST, request.FILES)
        if form.is_valid():
            msg = form.save()
            # return redirect(reverse('message_content', args=[msg.id]))
    else: 
        form = MessageToSelfForm(instance=profile)
    form = MessageToSelfForm()

    context = {'message_text_form': form}

    return render(request, 'dashboard/add_message_self_modal.html', context)


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

