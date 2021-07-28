from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    class Meta:
        # model = CustomUser
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'nickname']