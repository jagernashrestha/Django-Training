from django.shortcuts import render
from django.http import httpResponse
# Create your views here.
def recipie(request):
    return render(request, "recipie.html")