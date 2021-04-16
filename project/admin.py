from django.contrib import admin
from .models import Project, Category, Comment, Assign, Apply, Role

# Register your models here.
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Role)
admin.site.register(Apply)
