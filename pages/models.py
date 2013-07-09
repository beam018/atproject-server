from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext as _


PAGE_TYPES = (
    ('home', _('home')),
    ('about', _('about')),
    ('contacts', _('contacts')),
)


class Page(models.Model):
    title = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name=_('title'),
    )

    type = models.CharField(
        choices=PAGE_TYPES,
        verbose_name=_('type'),
        max_length=16,
        default='home',
    )

    thumb = models.ImageField(
        verbose_name=_('thumb'),
        upload_to='pages/thumbs',
        default='',
    )

    background = models.ImageField(
        verbose_name=_('background image'),
        upload_to='pages',
        default='',
    )

    content = RichTextField(
        blank=True,
        verbose_name=_('content'),
    )

    def __unicode__(self):
        return '%s' % self.title


    class Meta:
        verbose_name=_('page')
        verbose_name_plural=_('pages')