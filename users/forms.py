from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from .models import CustomUser

class CustomLoginForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','first_name','last_name','country')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'photo', 'about']
