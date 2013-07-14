from django.contrib import admin
from pages.models import Page

__author__ = 'beam'


class ProjectsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, ProjectsAdmin)
