from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'user_type', 'profile_picture', 'bio', 'skills', 'hourly_rate')

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','user_type','email', 'profile_picture', 'bio', 'skills', 'hourly_rate')