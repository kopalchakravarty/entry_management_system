from django import forms
from .models import *


class VisitorForm(forms.ModelForm):
    class Meta:
        model=Visitors
        fields=('name','phone','email','checkin','checkout')


class HostForm(forms.ModelForm):
    class Meta:
        model=Host
        fields=('name','phone','email')
