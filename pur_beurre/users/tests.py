"""Test management"""
from django.test import TestCase, client
from django.core import mail
from django.urls import reverse
from django.contrib.auth.models import User



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
        response = self.client.get('/logout/')
        self.assertRaises(KeyError, lambda: self.client.session['_auth_user_id'])
        self.assertEqual(response.status_code, 200)

    def test_change_password(self):
        self.client.login(username='user', password='password')
        response = self.client.post(reverse('change_form'),
                                    {'old_password1': 'password',
                                     'new_password1': 'test1234',
                                     'new_password2': 'test1234'}
                                    )
        self.assertEqual(response.status_code, 302)

    def test_reset_password(self):
        response = self.client.post(reverse('password_reset'),
                         {'email': 'test@mail.fr'}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('password_reset_done'))

    def test_favorite_view(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('favorite'))

        self.assertEqual(response.status_code, 302)


    def test_profile_view(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)




class EmailTests(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')