from rest_framework import serializers

from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','photo','email', 'country', 'about', 'pincode','role','event']