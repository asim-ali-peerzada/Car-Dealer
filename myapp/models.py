from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=500)
    