from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from extra_views import ModelFormSetView
from rest_framework import viewsets, permissions

from .forms import CustomUserCreationForm, CustomLoginForm, CustomUserChangeForm, PinCodeForm, AssignEventForm
from .models import CustomUser
from .serializers import UserSerializer

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class Login(auth_views.LoginView):
    authentication_form = CustomLoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')


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

class UpdatePinCodeView(generic.UpdateView):
    model = CustomUser
    form_class = PinCodeForm
    template_name = 'registration/pincode.html'
    success_url = reverse_lazy('home')

class AssignEventView(ModelFormSetView):
    model = CustomUser
    fields = ['event', 'role']
    template_name = "assign_event.html"
    factory_kwargs = {'extra': 0}
    # success_url = reverse_lazy('home')
    def get_queryset(self):
        return self.model.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
