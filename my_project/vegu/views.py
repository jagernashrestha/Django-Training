from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def recipe(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        recipe_image = request.FILES.get("recipe_image")
        description = data.get('description')
        
        Recipe.objects.create(
            name = name,
            description = description,
            recipe_image = recipe_image
        )
        return redirect  ('/recipe/')
    queryset = Recipe.objects.all()
    context = {"recipe":queryset}
    return render(request, "recipe.html", context )

def delete_recipe(request,id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipe/')
   