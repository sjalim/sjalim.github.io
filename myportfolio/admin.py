from django.contrib import admin
from .models import TodoItem 
from .models import HomeSidebarInfo, EducationItem, JobExperienceItem
# Register your models here.

admin.site.register(TodoItem)

admin.site.register(HomeSidebarInfo)

admin.site.register(EducationItem)

admin.register(JobExperienceItem)

