from rest_framework import serializers
from .models import *

class SecretMessageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SecretMessage
        fields = '__all__'

        