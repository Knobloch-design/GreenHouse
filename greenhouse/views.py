from django.shortcuts import render

# Create your views here.
# greenhouse/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'greenhouse/index.html', {'title': 'Home'})


def about(request):
    return render(request, 'greenhouse/about.html', {'title': 'About'})


def register(request):
    return render(request, 'greenhouse/register.html', {'title': 'Register'})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')

    return render(request, 'greenhouse/login.html')


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('user_login')


def dashboard(request):
    return render(request, 'greenhouse/dashboard.html')
