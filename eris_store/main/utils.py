from django.conf import settings
from django.db import models
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

from django.core.mail import send_mail

import random
import datetime


def recalc_cart(cart):
    cart_data = cart.products.aggregate(models.Sum('total_price'), models.Count('id'))
    if cart_data.get('total_price__sum'):
        cart.total_price = cart_data['total_price__sum']
    else:
        cart.total_price = 0
    cart.total_products = cart_data['id__count']
    cart.save()


class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):

        return (text_type(user.is_active) + text_type(user.pk) + text_type(timestamp))


account_activation_token = AppTokenGenerator()
