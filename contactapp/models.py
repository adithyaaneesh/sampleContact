from django.db import models
# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phonenumber = models.CharField(max_length=20,  blank=True, null=True)
    profile_image = models.ImageField(upload_to='photos/',null=True, blank=True)