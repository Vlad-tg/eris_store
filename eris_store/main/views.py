from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.db import transaction, IntegrityError
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import messages
from django.views.generic import DetailView, View, ListView
from numpy import random
import random
import numpy as np
from .models import Category, CartProduct, Customer, Product, VideoLaptop, OperatingSystemLaptop, RAM, CPULaptop, \
    SaleProductLaptop, User, Rating, RatingStar, BlogComment, Post, PromoCode, Cart
from .mixins import CategoryDetailMixin, CartMixin, AccountMixins
from .forms import OrderForm, LoginForm, RegistrationForm, ChangeInformationForm, ChangeIconForm, ChangeSequenceForm,\
    RatingForm
from .utils import recalc_cart
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.db.models import Count, Avg, Sum, F
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .filter_laptop import FilterLaptopView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from .utils import account_activation_token
from django.core.mail import EmailMessage


class AllView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        video_ones = VideoLaptop.objects.all(

        )
        products_sale_laptop = SaleProductLaptop.objects.all()
        products_sale_laptop_one = SaleProductLaptop.objects.filter(id=2)
        products_sale_laptop_three = SaleProductLaptop.objects.filter(id=4)
        if request.user.is_authenticated:
            user_id = Customer.objects.filter(user=request.user)
        else:
            user_id = Customer.objects.none()
        videos = VideoLaptop.objects.all()
        operating_systems = OperatingSystemLaptop.objects.all()
        product_laptop = Product.objects.all()
        context = {
            'queryset': queryset,
            'video_ones': video_ones,
            'operating_systems': operating_systems,
            'videos': videos,
            'products_laptop': product_laptop,
            'cart': self.cart,
            # 'page_obj': page_obj,
            'products_sale_laptop': products_sale_laptop,
            'products_sale_laptop_one': products_sale_laptop_one,
            'products_sale_laptop_three': products_sale_laptop_three,
            'user_id_html': user_id,

        }
        return render(request, 'main/all.html', context)


def product_rating(request, slug):
    if request.user.is_authenticated:
        user_id = Customer.objects.filter(user=request.user)
    else:
        user_id = Customer.objects.none()

    product = Product.objects.filter(slug=slug)
    products = Product.objects.filter(slug=slug).first()
    comments_html = BlogComment.objects.filter(product_comment=products, parent=None)
    star_form = RatingForm()
    rating_html = Rating.objects.filter(laptop__slug=slug).aggregate(total=Avg('star_id__value'))
    rating_count = Rating.objects.filter(laptop__slug=slug).aggregate(total=Count('star'))
    replies = BlogComment.objects.filter(product_comment=products).exclude(parent=None)
    reply_dict = {}
    for reply in replies:
        if reply.parent.sno not in reply_dict.keys():
            reply_dict[reply.parent.sno] = [reply]
        else:
            reply_dict[reply.parent.sno].append(reply)

    context = {
        'star_form': star_form,
        'rating_html': rating_html,
        'product_html': product,
        'user_id_html': user_id,
        'comments_html': comments_html,
        'reply_dict': reply_dict,
        'rating_count_html': rating_count,


    }
    return render(request, 'main/base.html', context)


class CategoryDetailView(AccountMixins,  CartMixin, CategoryDetailMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'main/category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        context['user_id_html'] = self.user_id
        return context


class CategoryFilterLaptopsView(AccountMixins, CartMixin, ListView):

    def get(self, request, *args, **kwargs):

        products = Product.objects.filter(category_id=1).order_by('id')
        videos = VideoLaptop.objects.all().order_by('-name')
        operating_systems = OperatingSystemLaptop.objects.all()
        rams = RAM.objects.all()
        processors = CPULaptop.objects.all().order_by('-name')
        screen_sizes = Product.objects.filter(category_id=1).values("screen_size").distinct()
        resolutions = Product.objects.filter(category_id=1).values("resolution").distinct()
        storage_drive_sizes = Product.objects.filter(category_id=1).values("storage_drive_size").distinct()

        paginator = Paginator(products, 1)
        number = request.GET.get('page', 1)
        page_obj = paginator.get_page(number)

        context = {
            'laptops': products,
            'videos': videos,
            'operating_systems': operating_systems,
            'rams': rams,
            'screen_sizes': screen_sizes,
            'resolutions': resolutions,
            'storage_drive_sizes': storage_drive_sizes,
            'processors': processors,
            'cart': self.cart,
            'user_id_html': self.user_id,
            'page_obj': page_obj,

        }
        return render(request, 'main/filter_laptop_category.html', context)


class AddToCartView(AccountMixins, CartMixin, View):
    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, product=product

        )
        if created:
            self.cart.products.add(cart_product)
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Product added successfully")
        return HttpResponseRedirect('/cart/')


class DeleteFromCartView(AccountMixins, CartMixin, View):
    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, product=product
        )
        self.cart.products.remove(cart_product)
        cart_product.delete()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Product delete successfully")
        return HttpResponseRedirect('/cart/')


class ChangeQTYView(AccountMixins, CartMixin, View):
    def post(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, product=product
        )
        qty = int(request.POST.get('qty'))
        cart_product.qty = qty
        cart_product.save()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Quantity successfully change")
        return HttpResponseRedirect('/cart/')


class CartView(FilterLaptopView, AccountMixins, CartMixin, View):

    def get(self, request, *args, **kwargs):
        prom_code = PromoCode.objects.all()
        context = {
            'codes': prom_code,
            'cart': self.cart,
            'user_id_html': self.user_id,

        }
        return render(request, 'main/cart.html', context)


class CheckoutView(AccountMixins, CartMixin, View):

    def get(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        context = {
            'cart': self.cart,
            'user_id_html': self.user_id,
            'form': form
        }
        return render(request, 'main/checkout.html', context)


class MakeOrderView(AccountMixins, CartMixin, View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        customer = Customer.objects.get(user=request.user)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.buying_type = form.cleaned_data['buying_type']
            new_order.order_date = form.cleaned_data['order_date']
            new_order.comment = form.cleaned_data['comment']
            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            new_order.save()
            customer.orders.add(new_order)
            messages.add_message(request, messages.INFO, 'thank you for the order')
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/checkout/')


class LoginView(CartView, View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'cart': self.cart,
        }

        return render(request, 'main/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {'form': form,
                   'cart': self.cart,
                   'user_id_html': self.user_id,
                   }
        return render(request, 'main/login.html', context)


class CreateAccountView(CartView, View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'cart': self.cart,

        }

        return render(request, 'main/create_account.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            Customer.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            email_body = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }

            link = reverse('activate', kwargs={
                'uidb64': email_body['uid'], 'token': email_body['token']})

            email_subject = 'Activate your account'

            activate_url = 'http://' + current_site.domain + link
            email = EmailMessage(
                email_subject,
                'Hi ' + user.username + ', Please the link below to activate your account \n' + activate_url,
                settings.EMAIL_HOST_USER,
                [new_user.email],
            )
            email.send(fail_silently=False)
            return HttpResponseRedirect('/login/')

        context = {
            'form': form,
            'cart': self.cart,
            'user_id_html': self.user_id,
        }
        return render(request, 'main/create_account.html', context)


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')


def is_valid_queryparam(param):
    return param != '' and param is not None


class SearchViews(AccountMixins, ListView):

    def get(self, request, *args, **kwargs):
        smartphone_search = Product.objects.filter(category_id=2)
        laptop_search = Product.objects.filter(category_id=1)
        product_qs = Product.objects.all()
        search_in = request.GET.get("search-in-product")

        if is_valid_queryparam(search_in):
            product_qs = product_qs.filter(title__icontains=search_in)

        context = {
            'user_id_html': self.user_id,
            'product_qs_html': product_qs,
            'smartphone_search_html': smartphone_search,
            'laptop_search_html': laptop_search

        }
        return render(request, 'main/search.html', context)


class TestSearchProductView(AccountMixins, DetailView):
    def get(self, request, *args, **kwargs):
        search_laptop = Product.objects.filter(category_id__name='laptop')
        smart_qs = Product.objects.filter(category_id__name='smartphone')
        head = Product.objects.filter(category_id__name='headphone')
        category = Category.objects.values('id')
        search_get_product = request.GET.get("search_product")
        min_get_product = request.GET.get("min_price_search")
        max_get_product = request.GET.get("max_price_search")
        choice_all_product = {
            "ALL PRODUCT": 100
        }
        laptop_get = request.GET.get("laptop")
        smartphone_get = request.GET.get("smartphone")
        headphone_get = request.GET.get("headphone")
        select_product_get = request.GET.get("select_product")

        if is_valid_queryparam(search_get_product and min_get_product and max_get_product and select_product_get):
            search_laptops = Product.objects.filter(
                Q(title__icontains=search_get_product) &
                Q(price__gte=min_get_product) &
                Q(price__lte=max_get_product) &
                Q(category_id__exact=select_product_get)

            ).distinct()
        else:
            search_laptops = Product.objects.filter(
                Q(title__icontains=search_get_product) &
                Q(price__gte=min_get_product) &
                Q(price__lte=max_get_product)
            ).distinct()

        context = {
            'result_list': search_laptops,
            'user_id_html': self.user_id,

        }

        return render(request, 'main/test003.html', context)


def account_view(request):

    if request.user.is_authenticated:
        user_id = Customer.objects.filter(user=request.user)
    else:
        user_id = Customer.objects.none()

    context = {

        'user_id_html': user_id,
    }

    return render(request, 'main/account.html', context)


def change_information_view(request):
    if request.user.is_authenticated:
        user_id_html = Customer.objects.filter(user=request.user)
    else:
        user_id_html = Customer.objects.none()
    user_id = Customer.objects.get(user=request.user)
    if request.method == "POST":
        form = ChangeInformationForm(request.POST or None)
        if form.is_valid():
            user_id.first_name = form.cleaned_data['first_name']
            user_id.last_name = form.cleaned_data['last_name']
            user_id.phone = form.cleaned_data['phone']
            user_id.address = form.cleaned_data['address']
            user_id.save()
        return HttpResponseRedirect(reverse('account'))
    form = ChangeInformationForm()

    context = {
        'form_information_html': form,
        'user_id_html': user_id_html,
        'user_id': user_id

    }

    return render(request, "main/edit.html", context)


def change_icon_view(request):
    if request.user.is_authenticated:
        user_id_html = Customer.objects.filter(user=request.user)
    else:
        user_id_html = Customer.objects.none()
    user_id = Customer.objects.get(user=request.user)
    if request.method == "POST":
        form = ChangeIconForm(request.POST, request.FILES)
        if form.is_valid():
            user_id.icon = form.cleaned_data['icon']
            user_id.save()
        return HttpResponseRedirect(reverse('account'))
    form = ChangeIconForm()

    context = {
        'form_icon_html': form,
        'user_id_html': user_id_html,
        'user_id': user_id

    }

    return render(request, "main/edit.html", context)


def change_sequence_view(request):
    if request.user.is_authenticated:
        user_id_html = Customer.objects.filter(user=request.user)
    else:
        user_id_html = Customer.objects.none()

    user_id = Customer.objects.get(user=request.user)
    if request.method == "POST":
        form = ChangeSequenceForm(request.POST, request.FILES)
        if form.is_valid():
            user_id.sequence = form.cleaned_data['sequence']
            user_id.save()
        return HttpResponseRedirect(reverse('account'))
    form = ChangeSequenceForm()

    context = {
        'form_sequence_html': form,
        'user_id_html': user_id_html,
        'user_id': user_id

    }

    return render(request, "main/edit.html", context)


class AddStarRatingView(AccountMixins, View):

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        user = request.user
        if form.is_valid():
            rating_main = Rating.objects.update_or_create(
                user=user,
                laptop_id=int(request.POST.get("product_id")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return rating_main


def post_comment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        parent_sno = request.POST.get('parentSno')
        if parent_sno == "":
            comment = BlogComment(comment=comment, user=user, product_comment=product)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parent_sno)
            comment = BlogComment(comment=comment, user=user, product_comment=product, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")

        comment.save()
        messages.success(request, "Your comment has been posted successfully")

    return redirect(f"/products/{product.slug}")


def leave_comment_and_rating_views(request, slug):
    star_form = RatingForm()
    product = Product.objects.filter(slug=slug)
    context = {
        'product_html': product,
        'star_form': star_form,

    }
    return render(request, "main/leave_comment_and_rating.html", context)


class SendCommentViews(AccountMixins, View):

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            comment = request.POST.get('comment')
            user = request.user
            product_id = request.POST.get('product_id')
            product = Product.objects.get(id=product_id)
            parent_sno = request.POST.get('parent_sno')
            if parent_sno == "":
                comment = BlogComment(comment=comment, user=user, product_comment=product)
                comment.save()
                messages.success(request, "Your comment has been posted successfully")
            else:
                parent = BlogComment.objects.get(sno=parent_sno)
                comment = BlogComment(comment=comment, user=user, product_comment=product, parent=parent)
                comment.save()
                messages.success(request, "Your reply has been posted successfully")

            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        return redirect(f"/products/{product.slug}")


class RandomView(AccountMixins, View):
    def get(self, request, *args, **kwargs):
        random_product = Product.objects.order_by('?').first()
        context = {
            'user_id_html': self.user_id,
        }

        return redirect(f"/products/{random_product.slug}", context)


class RandomProductERMAView(View):

    def get(self, request, *args, **kwargs):

        bow_item_d = list(Product.objects.all())
        random_list_item = np.random.choice(bow_item_d, 1, p=[0.5, 0.03, 0.05, 0.06, 0.08, 0.04, 0.05, 0.09, 0.05, 0.05])
        erma = Customer.objects.filter(user=request.user).values('virtual_money')

        if random_list_item:
            try:
                minus_erma = Customer.objects.get(user=request.user)
                minus_erma.virtual_money = F('virtual_money') - 50
                minus_erma.save()
            except IntegrityError:
                minus_erma = Customer.objects.get(user=request.user)
                minus_erma.virtual_money = 0
                minus_erma.save()
                return redirect(f"/account/")
        else:
            return redirect(f"/account/")

        context = {
            'random_product': random_list_item,
        }
        return render(request, 'main/random_product.html', context)


def promo_cod_view(request):
    if request.method == "GET":
        prom_text = request.GET.get('promo_codes')
        customers = Customer.objects.get(user=request.user)
        prom_code = PromoCode.objects.all()
        for codes in prom_code:
            if prom_text == codes.code:
                cart_prom_code = Cart.objects.get(owner=customers)
                cart_prom_code.total_price = F('total_price') - F('total_price') * codes.percent
                cart_prom_code.save()
                cart_code = codes
                cart_code.delete()
                messages.success(request, "This promo code successful actives")
                break
        else:
            cart_prom_code = Cart.objects.get(owner=customers)
            cart_prom_code.total_price = F('total_price')
            cart_prom_code.save()
            messages.success(request, "Don't wrong promo code")
    return redirect(f"/cart/")

