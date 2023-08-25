from django.db import models

import datetime
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django import forms
from django.db import models
from django.contrib.auth.models import User#, Problem
from django.urls import reverse


class Testimonial(models.Model):
	name = models.CharField(max_length=200)
	review = models.CharField(max_length=2000, null=True)

	def __str__(self):
		return self.name
