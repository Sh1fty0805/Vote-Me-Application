from django.contrib import admin
from .models import UserProfile, Candidate
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Candidate)