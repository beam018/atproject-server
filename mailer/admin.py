from django.contrib import admin
from mailer.models import Mail

__author__ = 'beam'


class MailAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mail, MailAdmin)