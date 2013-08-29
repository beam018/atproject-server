from django.db import models
from django.utils.translation import ugettext as _

import datetime


class PostType(models.Model):
    title = models.CharField(
        max_length=140,
        verbose_name=_('title'),
    )

    def __unicode__(self):
      return '%s' % self.title


    class Meta:
      verbose_name=_('post type')
      verbose_name_plural=_('post types')


class PostPlace(models.Model):
    title = models.CharField(
        max_length=140,
        verbose_name=_('title'),
    )

    def __unicode__(self):
      return '%s' % self.title


    class Meta:
      verbose_name=_('post place')
      verbose_name_plural=_('post places')


class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('title'),
    )

    author = models.CharField(
        max_length=255,
        verbose_name=_('author'),
        blank=True,
    )

    link = models.URLField(
        verbose_name=_('link'),
    )

    pub_date = models.DateField(
        default=datetime.datetime.now(),
        verbose_name=_('publication date'),
    )

    post_type = models.ForeignKey(
        to=PostType,
        max_length=140,
        blank=True,
        null=True,
        verbose_name=_('post type'),
    )

    pub_place = models.ForeignKey(
        to=PostPlace,
        max_length=140,
        blank=True,
        null=True,
        verbose_name=_('publication place'),
    )

    def __unicode__(self):
      return '%s' % self.title


    class Meta:
      verbose_name=_('post')
      verbose_name_plural=_('posts')
