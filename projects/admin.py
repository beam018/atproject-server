from django.contrib import admin
from projects.models import Project

__author__ = 'beam'


class ProjectsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectsAdmin)
