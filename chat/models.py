from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):

    date_created = models.DateTimeField(default=timezone.now)


class Chats(models.Model):

    username = models.CharField(max_length=150)
    chat_message = models.CharField(max_length=200)
    message_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ('message_timestamp',)
