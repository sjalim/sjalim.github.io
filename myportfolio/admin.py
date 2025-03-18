from django.contrib import admin
from .models import TodoItem 
from .models import HomeSidebarInfo
# Register your models here.

admin.site.register(TodoItem)

admin.site.register(HomeSidebarInfo)