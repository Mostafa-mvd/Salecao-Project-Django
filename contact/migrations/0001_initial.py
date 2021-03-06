# Generated by Django 3.2 on 2021-05-02 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=50, verbose_name='name')),
                ('subject', models.CharField(max_length=250, verbose_name='subject')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('message', models.TextField()),
                ('send_message_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='sent')),
            ],
        ),
    ]
