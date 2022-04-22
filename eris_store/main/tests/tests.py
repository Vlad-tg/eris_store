from django.test import TestCase
import pytest
from main.models import Product, Brand
from django.urls import reverse, resolve


class TestUrl:
    def test_url(self):

        path = reverse('base_product', kwargs={'slug': "apple-iphone-11-pro-max"})
        assert resolve(path).view_name == 'base_product'


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(name="Div", slug="div_d")

    def test_models(self):
        product = Brand.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 250)









