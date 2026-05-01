"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from first.views import first_fun,second_fun,contact,about
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',first_fun, name = "hello"),
    path('second/',second_fun, name = "success"),
    path('contact/',contact, name = "contact_page"),
    path('about/', about, name = "about_page" ),
]
