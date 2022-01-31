from django.contrib import admin
from .models import UserPreferences, MindfulCheck, Message

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


admin.site.register(UserPreferences, UserPreferencesAdmin)
admin.site.register(MindfulCheck, MindfulCheckAdmin)
admin.site.register(Message, MessageAdmin)
