"""Test management"""
from django.test import TestCase, client
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import update_session_auth_hash


# Create your tests here.
class UserViewTests(TestCase):

    def setUp(self):
        user = User.objects.create(username='user', password="password")

    def test_login(self):
        response = self.client.post(reverse('login'),
                                    {'username': 'user',
                                     'password': 'password'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.post(reverse('register'),
                                    {'username': 'user',
                                     'email': 'testuser@email.com',
                                     'password1': 'password',
                                     'password2': 'password'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):

        self.client.login(username='user', password='password')
        self.client.logout()
        self.assertRaises(KeyError, lambda: self.client.session['_auth_user_id'])

    def test_change_password(self):
        self.client.login(username='user', password='password')
        response = self.client.post(reverse('change_form'),
                                    {'old_password1': 'password',
                                     'new_password1': 'test1234',
                                     'new_password2': 'test1234'}
                                    )
        self.assertEqual(response.status_code, 302)
