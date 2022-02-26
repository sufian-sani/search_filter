from django import forms
from .models import *

class TimeRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}),required=False)
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}),required=False)

    fields = ['start_date', 'end_date']
