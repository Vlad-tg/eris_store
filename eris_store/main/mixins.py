from django.views.generic.detail import SingleObjectMixin
from .views import View
from django.db.models import Count, Q
from django.db import models

from .models import Category, Cart, Customer, Product, VideoLaptop, OperatingSystemLaptop, Compare


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


class CategoryDetailMixin(SingleObjectMixin):

    CATEGORY_SLUG2PRODUCT_MODEL = {
        'Product': Product
    }

    def get_context_data(self, **kwargs):
        if isinstance(self.get_object(), Category):
            model = self.CATEGORY_SLUG2PRODUCT_MODEL[self.get_object().slug]
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.get_categories_for_left_sidebar()
            context['category_products'] = model.objects.all()
            return context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get_categories_for_left_sidebar()
        return context


class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            if not customer:
                customer = Customer.objects.create(
                    user=request.user
                )
            cart = Cart.objects.filter(owner=customer, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
        else:
            cart = Cart.objects.filter(for_anonymous_user=True).first()
            if not cart:
                cart = Cart.objects.create(for_anonymous_user=True)
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)


class AccountMixins(View):
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            user_id = Customer.objects.filter(user=request.user)
        else:
            user_id = Customer.objects.none()
        self.user_id = user_id
        return super().dispatch(request, *args, **kwargs)


