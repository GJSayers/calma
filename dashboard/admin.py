from django.contrib import admin
from .models import UserPreferences, MindfulCheck, Message, Activities

# Register your models here.
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'preferences'
    )

class MindfulCheckAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'check_date',
        'purpose',
        'emotional',
        'financial',
        'physical',
        'social',
        'community',
        'career',
        'overall',
    )

class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'message_text',
    )

class ActivitiesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'preferences',
        'vid_length',
        'content',
    )

admin.site.register(UserPreferences, UserPreferencesAdmin)
admin.site.register(MindfulCheck, MindfulCheckAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Activities, ActivitiesAdmin)