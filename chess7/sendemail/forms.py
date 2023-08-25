# sendemail/forms.py
from django import forms
from django.forms import ModelForm
from sendemail.models import Message


class ContactForm(ModelForm):
    class Meta:
    	model = Message
    	fields = ['email_add', 'sender', 'subject', 'message']
