from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.
class SecretMessageView(generics.ListCreateAPIView):
    queryset = SecretMessage.objects.all()
    serializer_class = SecretMessageSerializer