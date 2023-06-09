from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SecretMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title