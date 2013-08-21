# -*- coding: utf-8 -*-

from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from filebrowser.fields import FileBrowseField


class City(models.Model):
    city_name = models.CharField(
        max_length=140,
        verbose_name=_('City name'),
    )

    def __unicode__(self):
        return self.city_name


    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')


class JobCategory(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Job category name'),
    )

    thumb = FileBrowseField(
        verbose_name=_('Job category thumbnail'),
        max_length=32,
    )

    background = FileBrowseField(
        blank=True,
        verbose_name=_('Job category background image'),
        max_length=32,
    )

    content = RichTextField(
        blank=True,
        verbose_name=_('Content'),
    )

    no_jobs_text = RichTextField(
        blank=True,
        verbose_name=_('no jobs text'),
        help_text=_("this text has displayed if category has no jobs"),
    )

    order_number = models.IntegerField(
        max_length=2,
        verbose_name=_('order number'),
        help_text=_('position number on first career page'),
        default=0,
    )

    def __unicode__(self):
        return self.name


    class Meta:
        verbose_name = _('job category')
        verbose_name_plural = _('job categories')


JOB_STATUSES = (
    ('p', _('Published')),
    ('np', _('Not published')),
    ('c', _('Close')),
)


class Job(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Job name'),
    )

    project = models.CharField(
        max_length=255,
        default='',
        blank=True,
        null=True,
        verbose_name=_('Project name'),
    )

    city = models.ForeignKey(
        to=City,
        blank=True,
        null=True,
        verbose_name=_('City'),
    )

    category = models.ForeignKey(
        to=JobCategory,
        null=True,
        verbose_name=_('Job category'),
    )

    employer = models.CharField(
        max_length=140,
        blank=True,
        verbose_name=_('Employer'),
    )

    status = models.CharField(
        max_length=2,
        default='p',
        choices=JOB_STATUSES,
        verbose_name=_('Status'),
    )

    top_content = RichTextField(
        blank=True,
        verbose_name=_('Top content'),
    )

    requirements = RichTextField(
        blank=True,
        verbose_name=_('Requirements'),
    )

    skills = RichTextField(
        blank=True,
        verbose_name=_('Skills'),
    )

    desired_skills = RichTextField(
        blank=True,
        verbose_name=_('Desired skills'),
    )

    bottom_content = RichTextField(
        blank=True,
        verbose_name=_('Bottom content'),
    )

    creation_date = models.DateTimeField(
        default=datetime.now(),
        editable=False,
        verbose_name=_('Creation date'),
    )

    user = models.ForeignKey(
        to=User,
        blank=True,
        null=True,
        editable=False,
        default=None,
        verbose_name=_('User'),
    )

    mailer = models.TextField(
        default='',
        blank=True,
        null=True,
        verbose_name=_('Mailing list'),
    )

    def __unicode__(self):
        return self.name


    class Meta:
        verbose_name = _('job')
        verbose_name_plural = _('jobs')