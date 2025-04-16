from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("education/", views.education, name="education"),
    path("skill/", views.skill, name="skill"),
    path("achievement/", views.achievement, name="achievement"),
    path("job_experience/", views.job_experience, name="job_experience"),
    path("project/", views.project, name="project"),
    path("research/", views.research, name="research"),
    path("publicaiton/", views.publication, name="publication"),
   path("resume/", views.resume, name="resume"),
    path("contact/", views.contact, name="contact"),
    path("todos/", views.todos, name="Todos"),

]