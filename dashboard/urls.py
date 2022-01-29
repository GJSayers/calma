from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', views.user_prefs, name='dashboard'),
    path('', views.message_self, name='dashboard'),
    path('', views.activities, name='dashboard')
]

