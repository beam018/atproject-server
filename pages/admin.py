from django.contrib import admin
from pages.models import Page, PageType

admin.site.register(PageType)
admin.site.register(Page)