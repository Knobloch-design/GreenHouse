from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.
from django.contrib.auth import login

from .models import ControlSignals


def home(request):
    return render(request, "main/home.html", {})


# TODO Change sign_up to register
def sign_up(request):
    if request.method == "POST":
        # if this is a POST request we need to process the form data
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            user = (
                form.save()
            )  # This is the line that creates the user and saves to the database
            login(request, user)  # This is the line that logs the user in
            return redirect(
                "home"
            )  # This is the line that redirects the user to the home page
    else:
        # if a GET (or any other method) we'll create a blank form
        form = RegistrationForm()

    return render(request, "registration/sign_up.html", {"form": form})

# backend/Main/views.py


def control_signals_status(request):
    control_signals = ControlSignals.objects.last()  # Get the latest control signal entry
    return render(request, 'main/controll_signals.html', {'control_signals': control_signals})

from main.MQTT_SUB import formatted_data,data_lock, mqtt_client
def live_data(request):
    global formatted_data, data_lock, mqtt_client
    print("live_data")
    print("formatted_data",formatted_data)
    print("mqtt_client",mqtt_client.get_last_data())
    print("mqtt_client",mqtt_client)
    live_data = mqtt_client.last_data  # Safely access formatted_data
    return render(request, 'main/live_data.html', {'live_data': live_data})