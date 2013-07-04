from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext as _


class PageType(models.Model):
    name = models.CharField(
        max_length=140,
        verbose_name=_('name'),
        unique=True,
    )

    def __unicode__(self):
        return '%s' % self.name


class Page(models.Model):
    title = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name=_('title'),
    )

    type = models.ForeignKey(
        PageType,
        verbose_name=_('type'),
        to_field='name',
    )

    thumb = models.ImageField(
        verbose_name=_('thumb'),
        upload_to='pages',
    )

    content = RichTextField(
        blank=True,
        verbose_name=_('content'),
    )

    def __unicode__(self):
        return '%s' % self.title