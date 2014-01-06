from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld


class FlatPageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())


    class Meta:
        model = FlatPage


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatPageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)