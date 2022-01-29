from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_prefs, name='dashboard'),
    path('', views.message_self, name='dashboard')
]