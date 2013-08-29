# -*- coding: utf-8 -*-

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext as _
from filebrowser.fields import FileBrowseField

PAGE_TYPES = (
    ('home', _('home')),
    ('posts', _('posts')),
    ('about', _('about')),
    ('contacts', _('contacts')),
    ('projects', _('projects')),
    ('404', _('404')),
)


class Page(models.Model):
    thumb = FileBrowseField(
        verbose_name=_('page thumbnail'),
        max_length=32,
    )

    image = FileBrowseField(
        verbose_name=_('page image'),
        max_length=32,
    )

    caption = models.CharField(
        max_length=255,
        verbose_name=_('Caption')
    )

    content = RichTextField(
        blank=True,
        verbose_name=_('Content'),
    )

    type = models.CharField(
        choices=PAGE_TYPES,
        verbose_name=_('type'),
        max_length=16,
        default='home',
    )

    order_number = models.IntegerField(
        max_length=2,
        verbose_name=_('order number'),
        default=0,
    )

    def __unicode__(self):
        return self.caption

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')