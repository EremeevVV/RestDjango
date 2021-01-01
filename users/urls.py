from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [ path('', TemplateView.as_view(template_name='home.html'), name='home'),
                path('signup/', views.SignUp.as_view(), name='signup'),
               path('login/', views.Login.as_view(),name='login'),
               path('logout/', auth_views.LogoutView.as_view(), name='logout'),
               path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
               path('password_change/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
               path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
               path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
               path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
               path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
               path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
               path('update/<int:pk>/',views.UpdateUserView.as_view(), name='update'),
                path('pinupdate/<int:pk>/', views.UpdatePinCodeView.as_view(), name="pin"),
                path('events/',views.AssignEventView.as_view(),name='events'),
                path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                ]

urlpatterns += static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)
