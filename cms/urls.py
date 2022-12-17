from django.urls import path
from cms import views



urlpatterns = [
    path('createpl', views.CreateProtectionLevel.as_view()),
]