from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class video1(models.Model):
    video = models.ImageField(null = True,blank = True, upload_to = '')

    def __str__(self):
        return self.video

class contact_det(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    company = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    message = models.CharField(max_length=255,null=True)
