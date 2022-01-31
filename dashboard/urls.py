from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('mindful-check/', views.mindful_check, name='mindful_check')
]