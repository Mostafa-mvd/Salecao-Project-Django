from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    created_time = models.DateTimeField(verbose_name="created", auto_now_add=True)
    title = models.CharField(max_length=250, verbose_name="title")
    creator = models.ForeignKey(User, verbose_name="creator", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="content")
