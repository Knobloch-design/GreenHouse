from django.urls import path
from . import views  # Import your CustomLoginView

urlpatterns = [
    # path('', views.home, name='home'),  # Add other URLs as needed
    # path('about/', views.about, name='about'),
    # path('login/', CustomLoginView.as_view(), name='login'),  # Use CustomLoginView for login
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("signup", views.sign_up, name="sign_up"),
]
