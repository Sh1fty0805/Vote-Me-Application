from django.db import models
from django.contrib.auth.models import User
 
class UserProfile(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    CITY_CHOICES = [
        ('Manila', 'Manila'),
        ('Cebu City', 'Cebu City'),
        ('Davao City', 'Davao City'),
        ('Baguio', 'Baguio'),
        ('Iloilo City', 'Iloilo City'),
        # Add more as needed
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, default="Unknown")
    birthdate = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default="Other")
    city = models.CharField(max_length=100, choices=CITY_CHOICES, default="Manila")
    address = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)  # optional email for newsletters

    def __str__(self):
        return self.user.username


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    platform = models.TextField()
    controversies = models.TextField(blank=True)
    resume = models.TextField()
    interview_links = models.URLField(blank=True)
    area_coverage = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.position}"

