from django import forms
from .models import *
class linkForm(forms.ModelForm):
    class Meta:
        model = link
        fields = ('url',)