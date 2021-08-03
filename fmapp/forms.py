from django import forms
from .models import Community

class PostForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title', 'body']

class SearchForm(forms.Form):
    check_values = forms.BooleanField(required=False)
