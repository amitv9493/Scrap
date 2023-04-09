from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = "register.html"

class register(TemplateView):
    template_name = "index.html"
