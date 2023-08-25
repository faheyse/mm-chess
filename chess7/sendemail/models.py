from django.db import models

# Create your models here.
class Message(models.Model):

	email_add = models.EmailField(max_length=200)
	sender = models.CharField(max_length=200)
	subject = models.CharField(max_length=200)
	message = models.CharField(max_length=200)

	def __str__(self):
		return self.sender