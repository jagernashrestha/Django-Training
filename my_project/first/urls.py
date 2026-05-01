from django.urls import path
from . import views

urlpatterns = [
    path('first/hello', views.say_hello()),
]