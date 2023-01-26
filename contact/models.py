from django.db import models
from django.contrib.auth.models import User


class video1(models.Model):
    video_file = models.FileField(upload_to='videos/',null= True)

    

class contact_det(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    company = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    message = models.CharField(max_length=255,null=True)
