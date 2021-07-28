from django import forms
from .models import Community, ComHospital, Qna

class PostForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title', 'body']

class PostFormm(forms.ModelForm):
    class Meta:
        model = ComHospital
        fields = ['title', 'body']

class PostFormmm(forms.ModelForm):
    class Meta:
        model = Qna
        fields = ['title', 'body']
        