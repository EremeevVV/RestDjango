from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

class Event(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class CustomUser(AbstractBaseUser, PermissionsMixin):
    url_height = models.PositiveIntegerField(null=True)
    url_width = models.PositiveIntegerField(null=True)
    first_name = models.CharField("user's first name", max_length=30)
    last_name = models.CharField("user's last name", max_length=30)
    photo = models.ImageField(default="usernophoto.jpg", width_field='url_width', height_field='url_height', upload_to='user_photos',
                              null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    country = models.CharField(max_length=300, choices=(
        ('US', 'United States'),
        ('FR', 'France'),
        ('CN', 'China'),
        ('RU', 'Russia'),
        ('IT', 'Italy')
    )
                               )
    about = models.TextField(verbose_name='about', null=True, blank=True, max_length=300)
    pincode = models.CharField(max_length=4,blank=True)
    role = models.CharField(max_length=300, choices=(
        ('A', 'Admin'),
        ('E', 'Expert'),
        ('C', 'Competitor'),
        ('N', 'No role'),
    )
                            ,default=('N', 'No role'))
    event = models.ForeignKey(Event, on_delete=models.SET_NULL,null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()

    class Meta():
        ordering = ['date_joined']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.last_name
