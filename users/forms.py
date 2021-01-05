from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from django import forms
from django.core.validators import RegexValidator

from .models import CustomUser

class CustomLoginForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','first_name','last_name','country','photo')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'country', 'photo', 'about']

class PinCodeForm(UserChangeForm):
    pincode = forms.CharField(max_length=4, validators=[RegexValidator(regex=r'^\d{4}$',
                                                                       message='PinCode must contain 4 digits / Пинкод должен состоять из 4 цифр',
                                                                       code='Wrong_Pin_Regex')],
                              help_text="PinCode must contain 4 digits")
    class Meta:
        model = CustomUser
        fields = ['pincode']

class AssignEventForm(UserChangeForm):
    class Meta():
        model = CustomUser
        fields = ['event', 'role']

    def remove_event(self):
        return self.fields['event'].value
