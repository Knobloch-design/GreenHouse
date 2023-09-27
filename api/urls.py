from django.urls import path
from .views import CustomLoginView  # Import your CustomLoginView

urlpatterns = [
    # path('', views.home, name='home'),  # Add other URLs as needed
    # path('about/', views.about, name='about'),
    path('login/', CustomLoginView.as_view(), name='login'),  # Use CustomLoginView for login
]
