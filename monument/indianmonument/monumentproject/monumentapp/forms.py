from django import forms
from .models import Monument



class MonuForm(forms.ModelForm):
    class Meta:
        model=Monument
        fields=['name','about','year','image']
