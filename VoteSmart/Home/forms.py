from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=255)
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    sex = forms.ChoiceField(choices=UserProfile.SEX_CHOICES)
    city = forms.ChoiceField(choices=UserProfile.CITY_CHOICES)
    address = forms.CharField(max_length=255)
    email = forms.EmailField(required=False, label="Email (optional, for newsletters)")

    class Meta:
        model = User
        fields = [
            'username', 'password1', 'password2',
            'full_name', 'birthdate', 'sex', 'city', 'address', 'email'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                birthdate=self.cleaned_data['birthdate'],
                sex=self.cleaned_data['sex'],
                city=self.cleaned_data['city'],
                address=self.cleaned_data['address'],
                email=self.cleaned_data['email']
            )
        return user