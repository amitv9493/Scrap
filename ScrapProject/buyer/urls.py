from django.urls import path
from .views import *
urlpatterns = [
    path("new/",register.as_view(), name = 'register')
]
