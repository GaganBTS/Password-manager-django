from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
class Passwordform(forms.ModelForm):
    class Meta:
        model= Passwords
        exclude=['user']
        widgets = {
            'website':forms.TextInput(attrs={'placeholder':'amazon.netflix,spotify etc.'}),
           'password': forms.PasswordInput(attrs={'placeholder':'*****','data-toggle':'password'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Your Name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Your Email'}),
            'message':forms.Textarea(attrs={'placeholder':'Your message'})
        }
   