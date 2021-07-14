from django.db import models

# Create your models here.


class OurServices(models.Model):
    name = models.CharField(verbose_name="service_name", max_length=100)
    content = models.TextField(max_length=400)
