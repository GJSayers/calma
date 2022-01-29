from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from djchoices import DjangoChoices, ChoiceItem


class UserPreferences(models.Model):
    """
    A user preferences model to determine the mindful dashboard preferences
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    WELLNESS_PREFS = (
        ('yoga', 'Yoga'),
        ('meditation', 'Meditation'),
        ('music', 'Music'),
        ('puzzles', 'Puzzles'),
        ('gaming', 'Gaming'),
        ('hiit', 'HIIT'),
        ('reading', 'Reading'),
    )

    preferences = MultiSelectField(max_length=100, choices=WELLNESS_PREFS)

    def __str__(self):
        return self.user.username


class MindfulCheck(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check_date = models.DateTimeField(auto_now_add=True)
    purpose = models.IntegerField(null=False, default=0)
    emotional = models.IntegerField(null=False, default=0)
    financial = models.IntegerField(null=False, default=0)
    physical = models.IntegerField(null=False, default=0)
    social = models.IntegerField(null=False, default=0)
    community = models.IntegerField(null=False, default=0)
    career = models.IntegerField(null=False, default=0)
    overall = models.DecimalField(null=True, decimal_places=2,
                                  max_digits=5, default=0)
        



class Message(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message_text = models.CharField(null=False, max_length=200)
