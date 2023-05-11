from django.contrib import admin
from .models import *
# Register your models here.
class SecretMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

admin.site.register(SecretMessage, SecretMessageAdmin)