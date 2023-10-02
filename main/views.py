from django.shortcuts import render, redirect
from .forms import RegistrationForm
# Create your views here.
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout

def home(request):
    return render(request, 'main/home.html', {})

#TODO Change sign_up to register
def sign_up(request):
    if request.method == 'POST':
        # if this is a POST request we need to process the form data
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            user = form.save() # This is the line that creates the user and saves to the database
            login(request, user) # This is the line that logs the user in
            return redirect('home') # This is the line that redirects the user to the home page
    else:
        # if a GET (or any other method) we'll create a blank form
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})


