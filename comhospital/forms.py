from django import forms
from .models import ComHospital

class PostForm(forms.ModelForm):
    class Meta:
        model = ComHospital
        fields = ['title', 'body']