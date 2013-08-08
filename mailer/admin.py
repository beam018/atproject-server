from django.contrib import admin
import reversion
from mailer.models import Mail

__author__ = 'beam'


class MailAdmin(reversion.VersionAdmin):
    pass


admin.site.register(Mail, MailAdmin)