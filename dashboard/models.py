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
    purpose = models.IntegerField(null=False, default=4)
    emotional = models.IntegerField(null=False, default=4)
    financial = models.IntegerField(null=False, default=4)
    physical = models.IntegerField(null=False, default=4)
    social = models.IntegerField(null=False, default=4)
    community = models.IntegerField(null=False, default=4)
    career = models.IntegerField(null=False, default=4)
    overall = models.DecimalField(null=True, decimal_places=2,
                                  max_digits=4, default=0)


class Message(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message_text = models.CharField(null=False, max_length=200)


class Activities(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.URLField(max_length=1024, null=False, blank=False)
    vid_length = models.CharField(max_length=12, null=False)
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
