from django import forms
from .models import Community

class PostForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title', 'body', 'pub_date']
        widgets = {
            'pub_date' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }