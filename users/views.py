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



class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'registration/profile.html'
    pk_url_kwarg = 'CustomUser_pk'

    def get_object(self, pk):
        return get_object_or_404(CustomUser, pk=pk)

class UpdateUserView(generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    # fields = ['first_name','last_name','photo','about']
    template_name = 'registration/update.html'

