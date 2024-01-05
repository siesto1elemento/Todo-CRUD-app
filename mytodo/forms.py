from django import forms
from .models import Task

class ModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['task','date_added','completed']