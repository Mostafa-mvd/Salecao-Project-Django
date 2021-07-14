from django.db import models
from django.utils import timezone


# Create your models here.


class Contact(models.Model):
    sender_name = models.CharField(verbose_name="name", max_length=50)
    subject = models.CharField(verbose_name="subject", max_length=250)
    email = models.CharField(verbose_name="email", max_length=100)
    message = models.TextField()
    send_message_time = models.DateTimeField(verbose_name="sent", default=timezone.now)

