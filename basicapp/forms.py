from django import forms
from django.core import validators
from .models import UserInfo,Lenden

class FormName(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name','email','verify_email','mobile_no','pan_no','dob']

class lendenform(forms.ModelForm):
    class Meta:
        model = Lenden
        fields = ['name','principal','rate','time']
