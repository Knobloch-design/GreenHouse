from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'greenhouse/login.html'  # Specify the path to your login template
    # You can add more customization options here, such as success and failure URLs, etc.
