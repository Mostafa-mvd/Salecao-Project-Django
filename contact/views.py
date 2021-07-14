from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def create_contact_form(request):
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
        else:
            messages.error(request, 'Invalid form submission.')
    return redirect("home:startup_page")
