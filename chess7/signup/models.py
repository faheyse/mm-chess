from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
from django.forms.widgets import DateInput
from django import forms
import ast

# Model for parent to sign up their child for a term
# Use in forms.py

# Should include parent name, child name, school, class,
# contact number, contact email, consent to photos, payment system

class School(models.Model):
	school_name = models.CharField(max_length=200)

	def __str__(self):
		return self.school_name


class Signup(models.Model):

	child_name = models.CharField(max_length=200)
	parent_name = models.CharField(max_length=200)
	contact_email = models.CharField(max_length=200)
	contact_num = models.IntegerField(max_length=10)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

	def __str__(self):
		return self.child_name


# add Term model
# includes dates for an entire term
# A term is school specific -> foreignkey:school
# in signup, a student should pay depending on which term they
# are entering which depends on which school they select

class DateArrayField(ArrayField):
    def formfield(self, **kwargs):
        kwargs['widget'] = forms.DateInput(attrs={'type': 'date'})
        return super().formfield(**kwargs)


class Term(models.Model):
	#title = models.CharField(max_length=200)
	# title ^ doesn't work for some reason??
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	#dates = DateArrayField(models.DateField())

	#Enter the dates in this format: DD-MM-YYYY_DD-MM-YYYY_... etc
	#Not the nicest solution but arrayfield was nasty
	dates = models.CharField(max_length=500)

	def __str__(self):
		return self.school.school_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)