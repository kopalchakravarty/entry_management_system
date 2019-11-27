from django import forms
from .models import *

# DEFINES FIELDS THAT NEED TO BE FILLED BY THE USER 

class VisitorForm(forms.ModelForm):  # VISITOR FIELDS
    class Meta:
        model=Visitors
        fields=('name','phone','email','checkin','checkout')


class HostForm(forms.ModelForm):  # HOST FIELDS
    class Meta:
        model=Host
        fields=('name','phone','email')
