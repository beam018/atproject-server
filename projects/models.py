# -*- coding: utf-8 -*-

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext as _

class Project(models.Model):
    thumb = models.ImageField(
        upload_to='thumbs',
        verbose_name=_('Project thumbnail'),
    )

    image = models.ImageField(
        upload_to='projects',
        verbose_name=_('Project image'),
    )

    caption = models.CharField(
        max_length=255,
        verbose_name=_('Caption')
    )

    content = RichTextField(
        blank=True,
        verbose_name=_('Content'),
    )

    def __unicode__(self):
        return self.caption

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')