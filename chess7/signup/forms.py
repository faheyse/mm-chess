from django import forms
from django.forms import ModelForm
from signup.models import Signup

class SignupForm(ModelForm):
	class Meta:
		model = Signup
		fields = ['child_name', 'parent_name', 'contact_email', 'contact_num', 'school']
