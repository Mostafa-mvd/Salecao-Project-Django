from django.urls import path
from . import views


app_name = 'startup'  # this out namespace

urlpatterns = [
    path("", views.startup_page, name="startup_page"),
]
