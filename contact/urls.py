from django.urls import path
from . import views


app_name = 'contact'  # this out namespace

urlpatterns = [
    path("", views.create_contact_form, name="contact_page"),
]

