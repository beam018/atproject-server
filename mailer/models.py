# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

MAIL_TYPES = (
    ('s', _('Staff')),
    ('c', _('Client')),
)


class Mail(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name=_('Mail title'),
    )

    template = models.TextField(
        verbose_name=_('Mail template')
    )

    type = models.CharField(
        max_length=1,
        default='s',
        choices=MAIL_TYPES,
        verbose_name=_('Mail type'),
    )

    def __unicode__(self):
        return '%s' % self.title


    class Meta:
        verbose_name = _('mail')
        verbose_name_plural = _('mails')