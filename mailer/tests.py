from django.test import TestCase
from django.test.client import Client
from django.core import mail
from django.http.request import HttpRequest
import copy
from mailer.models import Mail
from mailer.views import MailView


class ModelTest(TestCase):
    def setUp(self):
        self.model = Mail.objects.create(
            title='My title',
            template='',
            type='c',
        )

    def test_unicode_method(self):
        self.assertEqual(self.model.__unicode__(), 'My title')


class EmailTest(TestCase):
    fixtures = [
        'mailer_testdata.json',
    ]

    data = {
        'job_id': 1,
        'name': 'John',
        'surname': 'Dou',
        'phone': '89121234567',
        'email': 'user@example.com',
        'extra': 'lorem ipsum',
        'attachment': 'C:\\fakepath\\test.pdf'
    }

    def setUp(self):
        self.client = Client()

    def test_form_get(self):
        r = self.client.get('/mail/')
        self.assertEqual(r.status_code, 404)

    def test_form_post(self):
        r = self.client.post('/mail/', self.data)
        self.assertEqual(r.status_code, 200)

    def test_empty_form_submit(self):
        r = self.client.post('/mail/')
        self.assertEqual(r.status_code, 200)
        self.assertHTMLEqual(r.content, 'Data was broken.')

    def test_empty_field(self):
        for key in self.data:
            test_data = copy.copy(self.data)
            test_data[key] = ''

            r = self.client.post('/mail/', test_data)
            if key != 'extra':
                self.assertHTMLEqual(r.content, 'Data was broken.', msg=key + ' field is not handled')
            else:
                self.assertHTMLEqual(r.content, 'Data was transferred.', msg=key + ' field is not handled')

    def test_broken_request(self):
        for key in self.data:
            test_data = copy.copy(self.data)
            del test_data[key]

            r = self.client.post('/mail/', test_data)
            if key != 'extra':
                self.assertHTMLEqual(r.content, 'Data was broken.', msg=key + ' field is not handled')
            else:
                self.assertHTMLEqual(r.content, 'Data was transferred.', msg=key + ' field is not handled')

    def test_mail(self):
        self.client.post('/mail/', self.data)
        self.assertEqual(len(mail.outbox), 1)


class ValidationTest(TestCase):
    view = MailView()

    def setUp(self):
        self.client = Client()
        self.req = HttpRequest()

    def test_validation_extra(self):
        values = [
            'string',
            '',
            None,
            True,
            8999999999,
            100,
        ]

        for value in values:
            self.req.POST['extra'] = value
            self.assertEqual(self.view.validate_request(self.req), True)

    def test_validation_phone(self):
        valid = [
            '89121231212',
            '+79121231212',
            '8(912)1231212',
            '8(912)123-12-12',
            '8 (912) 123 12 12',
            '+8(812)1231212',
            '+8(912)123-12-12',
            '+8 (912) 123 12 12',
            '8 912 123 12 12',
            '+8 912 123 12 12',
        ]

        invalid = [
            'string',
            '',
            None,
            True,
            8999999999,
            100,
            '+8 912 123 12 12123123',
        ]

        for phone in valid:
            self.req.POST['phone'] = phone
            self.assertEqual(self.view.validate_request(self.req),True)

        for phone in invalid:
            self.req.POST['phone'] = phone
            self.assertEqual(self.view.validate_request(self.req),False)

    def test_validation_email(self):
        valid = [
            'user@example.com',
        ]

        invalid = [
            'localhost',
            '',
            None,
            True,
            1,
        ]

        for email in valid:
            self.req.POST['email'] = email
            self.assertEqual(self.view.validate_request(self.req), True)

        for email in invalid:
            self.req.POST['email'] = email
            self.assertEqual(self.view.validate_request(self.req), False)