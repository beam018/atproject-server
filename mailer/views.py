# -*- coding: UTF-8 -*-
import logging
import os
import re
import codecs

from django.core.mail.message import EmailMessage
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.core.validators import validate_email, RegexValidator
from django.core.exceptions import ValidationError

from career.models import Job
from mailer.models import Mail

from atserver.settings import MAILER_EMAIL_FROM

MAIL_TYPE_CLIENT = 'c'
MAIL_TYPE_STAFF = 's'

class MailView(View):
    @staticmethod
    def validate_request(request):
        """
        post validation

        rules:
            ✔ all listed fields must be filled
            ✔ email field must pass ([\w-\.]+)@((?:[\w]+\.)+)([a-zA-Z]{2,4})
            ✔ phone field must pass ^\+?[0-9]{1,3}[-. (]?\(?([0-9]{3})\)?[)-. ]?([0-9]{3})[-. ]?([0-9]{2})[-. ]?([0-9]{2})$

        fields(* - require):
            * name
            * surname
            * phone
            * email
            * attachment
            extra
        """
        r = request.POST

        for field, value in r.iteritems():
            if not field == 'extra':
                # all field exclude 'extra' must have value
                if not value:
                    return False

            if field == 'phone':
                regexp = re.compile(r"^\+?[0-9]{1,3}[-. (]?\(?([0-9]{3})\)?[)-. ]?([0-9]{3})[-. ]?([0-9]{2})[-. ]?([0-9]{2})$")
                validate_phone = RegexValidator(regex=regexp)
                try:
                    validate_phone(r['phone'])
                except (ValidationError, TypeError):
                    return False

            if field == 'email':
                try:
                    validate_email(r['email'])
                except (ValidationError, TypeError):
                    return False

        return True

    @staticmethod
    def get_fixture_data(file):
        return codecs.open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/',
                file
            ),
            'r', 'utf-8'
        ).read()

    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound()

    def post(self, request, *args, **kwargs):
        p = request.POST

        user_data = {}
        try:
            user_data['name'] = p['name']
            user_data['surname'] = p['surname']
            user_data['phone'] = p['phone']
            user_data['email'] = p['email']
            user_data['resume'] = p['resume']
        except KeyError:
            return HttpResponse('Data was broken.')

        try:
            user_data['extra'] = p['extra']
        except KeyError:
            user_data['extra'] = ''

        try:
            p['job_id']
        except KeyError:
            return HttpResponse('Data was broken.')

        if not self.validate_request(request):
            return HttpResponse('Data was broken.')

        job = Job.objects.get(pk=p['job_id'])

        msg, created = Mail.objects.get_or_create(
            type=MAIL_TYPE_CLIENT,
            defaults={
                'title': u"Allods team",
                'template': self.get_fixture_data('mail_user.txt'),
            }
        )
        if created:
            msg.save()

        # https://docs.djangoproject.com/en/dev/topics/email/#django.core.mail.EmailMessage
        message = EmailMessage(
            msg.title,
            msg.template.format(job=job),
            MAILER_EMAIL_FROM,
            [user_data['email'],]
        )
        message.send()

        staff_msg, created = Mail.objects.get_or_create(
            type=MAIL_TYPE_STAFF,
            defaults={
                'title': u'Заявка на вакансию {job.name} - {job.project} - {job.city}',
                'template': self.get_fixture_data('mail_staff.txt'),
            }
        )
        if created:
            staff_msg.save()

        staff_message = EmailMessage()
        staff_message.subject = staff_msg.title.format(job=job)

        staff_message.body = staff_msg.template.format(
            job = job,

            name = user_data['name'],
            surname = user_data['surname'],
            phone = user_data['phone'],
            email = user_data['email'],

            extra = user_data['extra'],
        )
        staff_message.from_email = MAILER_EMAIL_FROM

        tmp_file = None
        try:
            data = request.FILES['attachment']

            path = default_storage.save(
                'mail/%s' % request.FILES['attachment'],
                ContentFile(data.read())
            )
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        except Exception:
            pass

        if tmp_file:
            staff_message.attach_file(
                os.path.join(settings.MEDIA_ROOT, 'mail', tmp_file)
            )

        to_list = []
        if job.user:
            to_list.append(job.user.email)
        if job.mailer:
            to_list += job.mailer.split(', ')

        for to in to_list:
            try:
                validate_email(to)
                staff_message.to = [to,]
                staff_message.send()
            except ValidationError:
                logging.warning('wrong mail - %s' % to)

        return HttpResponse('Data was transferred.')
