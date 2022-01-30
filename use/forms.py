from dataclasses import fields
from pyexpat import model
from django import forms
from .models import userregister

class RegisterForm(forms.ModelForm):
    class Meta:
        model = userregister
        fields = ['email','password','password1','role']