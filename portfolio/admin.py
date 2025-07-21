from django.contrib import admin
from .models import TodoItem 
from .models import HomeSidebarInfo, EducationItem, JobExperienceItem, AchievementItem, Section, Categories, Skills
# Register your models here.

admin.site.register(TodoItem)

admin.site.register(HomeSidebarInfo)

admin.site.register(EducationItem)

admin.site.register(JobExperienceItem)

admin.site.register(AchievementItem)
admin.site.register(Section)
admin.site.register(Categories)

admin.site.register(Skills)
