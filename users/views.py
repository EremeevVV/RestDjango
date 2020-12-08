from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth import views as auth_views

from .forms import CustomUserCreationForm, CustomLoginForm,CustomUserChangeForm
from .models import CustomUser

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class Login(auth_views.LoginView):
    authentication_form = CustomLoginForm
    template_name = 'registration/login.html'
    # redirect_field_name = 'profile'



class ProfileView(generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/profile.html'


class UpdateUserView(generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/update.html'

