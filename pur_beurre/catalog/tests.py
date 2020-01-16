"""test management"""
from django.test import TestCase, client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category
from .fill_db import Fill_database

# Create your tests here.


class CatalogViewsTests(TestCase):

    def test_index_returns_200(self):
        response = self.client.get(reverse('catalog:index'))
        html = response.content.decode('utf8')

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('<strong>DU GRAS, OUI, MAIS DE LA QUALITÉ !</strong>', html)

    def test_credits_returns_200(self):
        response = self.client.get(reverse('catalog:credits'))
        self.assertEqual(response.status_code, 200)


class DataTests(TestCase):

    def setUp(self):
        user = User.objects.create(username='user', password="password")
        self.chocolat = Category.objects.create(name='chocolat')

        product = Product.objects.create(id=45623,
                                         name='Chocolat',
                                         category=self.chocolat,
                                         brand='casino',
                                         nutrition_grade='a',
                                         picture='chocolat.jpeg',
                                         nutrition_image='chocolatnutrigrade.com',
                                         url='www.chocolat.com'
                                         )

    def test_search_returns_200(self):
        chocolat = str('Chocolat')
        response = self.client.get(reverse('catalog:search'), {
            'query': chocolat,
        })
        self.assertEqual(response.status_code, 200)

    def test_search_page_redirect_302(self):
        chocolat = str('invalid name')
        response = self.client.get(reverse('catalog:search'), {
            'query': chocolat,
        })
        self.assertEqual(response.status_code, 302)

    def test_detail_page_returns_200(self):
        response = self.client.get('/substitute/45623/')
        self.assertEqual(response.status_code, 200)

    def test_save_favorite_returns_302(self):
        self.client.login(username='user', password='password')
        response = self.client.get('/favorite/')
        self.assertEqual(response.status_code, 302)

    def test_credits_page_return_200(self):
        response = self.client.get('/credits/')
        self.assertEqual(response.status_code, 200)


class Fill_databaseTest(TestCase):

    def setup(self):  # pragma: no cover
        self.c = Fill_database()
        self.c.create_db()

    def test_create_categorie(self):
        chocolat = Category.objects.filter(name='chocolat')
        self.assertIsNotNone(chocolat)

    def test_create_product(self):
        product = Product.objects.filter(category=2)
        self.assertIsNotNone(product)
