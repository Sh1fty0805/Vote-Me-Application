from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    address = models.CharField(max_length=255)
    citizenship = models.CharField(max_length=50)
    is_registered_voter = models.BooleanField(default=False)

    #http://127.0.0.1:8000/Home or Senators or 

    
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    platform = models.TextField()
    controversies = models.TextField(blank=True)
    resume = models.TextField()
    interview_links = models.URLField(blank=True)
    area_coverage = models.CharField(max_length=255)


