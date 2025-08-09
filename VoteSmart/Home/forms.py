from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(max_length=255)
    citizenship = forms.CharField(max_length=50)
    is_registered_voter = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 
                  'birthdate', 'address', 'citizenship', 'is_registered_voter']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                birthdate=self.cleaned_data['birthdate'],
                address=self.cleaned_data['address'],
                citizenship=self.cleaned_data['citizenship'],
                is_registered_voter=self.cleaned_data['is_registered_voter']
            )
        return user