from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.

def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def skill(request):
    return render(request, "skill.html")

def project(request):
    return render(request, "project.html")

def contact(request):
    return render(request, "contact.html")


