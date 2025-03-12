from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("skill/", views.skill, name="skill"),
    path("project/", views.project, name="project"),
    path("contact/", views.contact, name="contact")

]