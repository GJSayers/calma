from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_prefs, name='user_prefs'),
    path('', views.message_self, name='message_self')
]