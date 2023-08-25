from django.shortcuts import render

# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Message


def contactView(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()

            try:
                send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], form.cleaned_data['email_add'], ["manojlovic.mihailo@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            context = {
                "sender": form.cleaned_data['sender'],
            }
            return render(request, "sendemail/contact_success.html", {"form": form})
    else:
        form = ContactForm()

    #print("HEY"+form)
    return render(request, "sendemail/email.html", {"form": form})


def successView(request):
    return HttpResponse("Success! Thank you for your message.")
