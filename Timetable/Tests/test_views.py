from django.test import TestCase, Client
from django.urls import reverse, resolve
from Timetable.Register.models import Courses


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.confirm_log = reverse('confirm_log')
        self.reset = reverse('reset')
        self.forgot = reverse('forgot')
        self.Reg = reverse('Reg')

    def test_project_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Log_in.html')

    def test_confirm_login(self):
        response = self.client.get(self.confirm_log)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Loggedin.html')

    def test_forgot(self):
        response = self.client.get(self.forgot)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/forgot.html')

    def test_reset(self):
        response = self.client.get(self.reset)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/reset.html')
