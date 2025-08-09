from django.contrib import admin
from .models import TodoItem 
from .models import Publication, ProjectSection, Project, HomeSidebarInfo, EducationItem, JobExperienceItem, AchievementItem, Section, Categories, Skill

admin.site.register(TodoItem)

admin.site.register(HomeSidebarInfo)

admin.site.register(EducationItem)

admin.site.register(JobExperienceItem)

admin.site.register(AchievementItem)
admin.site.register(Section)
admin.site.register(Categories)

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ProjectSection)
admin.site.register(Publication)