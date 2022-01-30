from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('', views.user_prefs, name='user_prefs'),
    path('message-self/', views.message_self_content, name='message_self'),
    path('add-message-self/', views.add_message_self, name='add_message_self'),
    path('', views.activities, name='activities')
]

