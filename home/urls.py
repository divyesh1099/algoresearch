from django.urls import path
from .views import SecretMessageView
from home.apps import HomeConfig

app_name = 'home'

urlpatterns = [
    path('secretmessage/', SecretMessageView.as_view(), name = 'secret_message'),
]