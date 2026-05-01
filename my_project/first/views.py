from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Takes request->Returns Response
#Request handler
#action

def first_fun(request):
    peoples = [
    {"name" : "Jagerna", "age" :21},
    {"name" : "Pratik","age" :23},
    {"name" : "sharbes", "age" :22},
    {"name" : "ram", "age" : 24},
    ]
    text = """ Lorem ipsum dolor sit amet, consectetur adipisicing elit. Soluta porro nesciunt harum incidunt, doloremque aliquam, consequuntur nemo enim hic fugit a est placeat nulla necessitatibus dolor vitae obcaecati sed veritatis?"""

    vegetables = ["Tomato","potato","cucumber"]
    return render(request, "index.html",context ={'peoples':peoples,'text':text,"vegetables":vegetables})

def second_fun(request):
    return HttpResponse("This is success response")

def contact(request):
    return render(request,"contact.html")
    
def about(request):
    return render(request,"about.html")