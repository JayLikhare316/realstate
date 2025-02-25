from django.db import models

# Create your models here.
class AgentProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='agent')

class TeamProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team')
