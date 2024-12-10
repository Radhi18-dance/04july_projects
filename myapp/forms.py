from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=signmodel
        fields='__all__'
class updateform(forms.ModelForm):
    class Meta:
        model=signmodel
        fields=['fullname','mobile','email','password']

class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'

class contactForm(forms.ModelForm):
    class Meta:
        model=contactus
        fields='__all__'