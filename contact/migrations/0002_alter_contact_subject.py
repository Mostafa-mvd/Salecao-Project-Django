# Generated by Django 3.2 on 2021-05-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=250, verbose_name='subject'),
        ),
    ]
