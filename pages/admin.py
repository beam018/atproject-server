from django.contrib import admin
import reversion
from pages.models import Page

__author__ = 'beam'


class ProjectsAdmin(reversion.VersionAdmin):
    pass

admin.site.register(Page, ProjectsAdmin)
