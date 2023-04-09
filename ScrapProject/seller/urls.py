from django.urls import path
from .views import *
urlpatterns = [
    path("new/",registerView.as_view(), name = 'register')
]
