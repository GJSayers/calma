from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-message/', views.message_to_self, name='message_to_self'),
    path('update-prefs/', views.user_prefs, name='user_prefs'),
]