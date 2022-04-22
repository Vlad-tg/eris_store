
from django.db import models
from django.contrib.auth import get_user_model
from datetime import date, datetime, timezone
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.db.models import Count, Avg


User = get_user_model()


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


class Category(models.Model):
    name = models.CharField(verbose_name='Name category', max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Brand(models.Model):

    name = models.CharField(verbose_name='Brand', max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

#       --------------------------------  all ------------------------------------------------        #

    category = models.ForeignKey("Category", verbose_name='Category', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name='Brand', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Name', max_length=250)
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Imagine')
    description = models.TextField(verbose_name='description', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')
    total_rating = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Rating Star product')

#         ---------------------------------------------- laptop ------------------------           #

    by_series = models.ForeignKey('BySeriesLaptop', verbose_name='By series laptop',
                                  on_delete=models.CASCADE, null=True, blank=True)
    operating_system = models.ForeignKey('OperatingSystemLaptop', verbose_name='Operating system laptop'
                                         , on_delete=models.CASCADE, null=True, blank=True)
    screen_size = models.CharField(max_length=255, verbose_name='Screen size', blank=True)
    resolution = models.CharField(max_length=255, verbose_name='Resolution', null=False, blank=True)
    graphics = models.ForeignKey('VideoLaptop', verbose_name='Graphics', null=True, on_delete=models.CASCADE,
                                 blank=True)
    processor = models.ForeignKey('CPULaptop', verbose_name='CPU laptop', null=True, on_delete=models.CASCADE,
                                  blank=True)
    cpu_speed = models.CharField(max_length=255, verbose_name='CPU Speed', blank=True)
    cpu_core = models.CharField(max_length=255, verbose_name='CPU Core', blank=True)
    ram = models.ForeignKey('RAM', verbose_name='Memory(RAM)', null=True, on_delete=models.CASCADE, blank=True)
    storage_drive_size = models.CharField(max_length=255, verbose_name='Storage drive size', blank=True)
    touch = models.BooleanField(default=True, verbose_name='Touch/Non Touch')
    battery_charge = models.CharField(max_length=255, verbose_name='Battery life', blank=True)
    #         ---------------------------------------------- smartphone ------------------------           #
    operating_system_smartphone = models.ForeignKey('OperatingSystemSmartphone',
                                                    related_name='Operating System Smartphone+'
                                                    , on_delete=models.CASCADE, null=True, blank=True)
    diagonal = models.CharField(max_length=255, verbose_name='Diagonal', null=False, blank=True)
    resolution_smartphone = models.CharField(max_length=255, verbose_name='Resolution', null=False, blank=True)
    camera = models.CharField(max_length=255, verbose_name='Camera', null=False, blank=True)
    type_screen = models.CharField(max_length=255, verbose_name='Type screen', null=False, blank=True)
    processor_smartphone = models.ForeignKey('CPUSmartphone', verbose_name='CPU Smartphone', on_delete=models.CASCADE
                                             , null=True, blank=True)
    ram_smartphone = models.ForeignKey('RAM', verbose_name='RAM(smartphone)', related_name='RAM for smartphone+',
                                       on_delete=models.CASCADE, null=True, blank=True)
    battery_charge_smartphone = models.CharField(max_length=255, verbose_name='Battery charge', null=False, blank=True)
    sd = models.BooleanField(default=True, verbose_name='SD', null=False, blank=True)
    sd_volume_max = models.CharField(
        max_length=255, null=False, blank=True, verbose_name='Sd volume max'
    )
    #         ---------------------------------------------- headphone ------------------------           #
    color = models.CharField(max_length=255, verbose_name='Color', blank=True)
    fit_type = models.CharField(max_length=255, verbose_name='Fit type', blank=True)
    item_dimensions = models.CharField(max_length=255, verbose_name='Item dimensions', blank=True)
    item_weight = models.CharField(max_length=255, verbose_name='Item weight', blank=True)
    battery = models.CharField(max_length=255, verbose_name='Batteries', blank=True)

    def __str__(self):
        return "{} : {}.".format(self.category.name, self.title)

    def get_absolute_url(self):
        return reverse('base_product', kwargs={'slug': self.slug})

    def get_model_name(self):
        return self.__class__.__name__.lower()


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Customer', on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey(Product, verbose_name='Name product', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total Price')

    def __str__(self):
        return "Product: {} (for Cart)".format(self.product.title)

    def save(self, *args, **kwargs):
        self.total_price = self.qty * self.product.price
        super().save(*args, **kwargs)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', null=True, verbose_name='Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, default=0,  decimal_places=2, verbose_name='Total Price')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class CompareProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Customer', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name='Name product', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "Product: {} (for Compare)".format(self.product.title)


class Compare(models.Model):

    owner = models.ForeignKey('Customer', null=True, verbose_name='Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField(CompareProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Customer', on_delete=models.CASCADE)
    icon = models.ImageField(verbose_name='Icon', default='owner.png', upload_to='icon/')
    sequence = models.ImageField(verbose_name='Sequence', default='sequence.jpg', upload_to='sequence/')
    phone = models.CharField(max_length=20, verbose_name='Phone', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Address', null=True, blank=True)
    orders = models.ManyToManyField('Order', verbose_name='Buyers orders', related_name='related_customer')
    virtual_money = models.PositiveIntegerField(verbose_name='Virtual money(erma)', default=0, null=True, blank=True)

    def __str__(self):
        return "Customer: {} {}".format(self.user.first_name, self.user.last_name)


class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'pickup'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'New order'),
        (STATUS_IN_PROGRESS, 'Order in progress'),
        (STATUS_READY, 'Order is ready'),
        (STATUS_COMPLETED, 'Order completed')
    )
    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Pickup'),
        (BUYING_TYPE_DELIVERY, 'Delivery')
    )

    customer = models.ForeignKey(Customer, verbose_name='Customer', related_name='related_orders',
                                 on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Name')
    last_name = models.CharField(max_length=255, verbose_name='Last name')
    phone = models.CharField(max_length=255, verbose_name='Phone')
    cart = models.ForeignKey(Cart, verbose_name='Cart', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Address', null=True, blank=True)
    status = models.CharField(
        max_length=255,
        verbose_name='Status is order',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=255,
        verbose_name='Order type',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Order comment', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    order_date = models.DateField(verbose_name='Date of receipt of the order', default=timezone.now)

    def __str__(self):
        return str(self.id)


class VideoLaptop(models.Model):
    name = models.CharField(verbose_name="Video Laptop", max_length=255,)
    slug = models.SlugField(verbose_name="Slug", allow_unicode=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('filter', kwargs={'slug': self.name})


class VideoSmartphone(models.Model):
    name = models.CharField(verbose_name='Name video laptop or computer', max_length=255, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class CPUSmartphone(models.Model):
    name = models.CharField(verbose_name='Name processor smartphone or computer', max_length=255, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class CPULaptop(models.Model):
    name = models.CharField(verbose_name='Name processor laptop or computer', max_length=255, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class CPUSpeedLaptop(models.Model):
    name = models.CharField(verbose_name='CPU Speed', max_length=255, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class CPUCoreLaptop(models.Model):
    name = models.CharField(verbose_name='CPU Core', max_length=255, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class RAM(models.Model):
    name = models.CharField(verbose_name='Name RUM', max_length=255, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class OperatingSystemSmartphone(models.Model):
    name = models.CharField(verbose_name='Name operating system smartphone', max_length=255, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class OperatingSystemLaptop(models.Model):
    name = models.CharField(verbose_name='Name operating system laptop or computer', max_length=255, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('filter', kwargs={'slug': self.name})


class BySeriesLaptop(models.Model):
    name = models.CharField(verbose_name='By series', max_length=255, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ResolutionLaptop(models.Model):
    name = models.CharField(verbose_name='Resolution', max_length=255, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ScreenSizeLaptop(models.Model):
    name = models.CharField(verbose_name='Screen Size', max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class SaleProductLaptop(models.Model):

    products_name = models.ForeignKey(Product, verbose_name='Laptop(sale)', on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price Discount')

    def __str__(self):
        return "{} : {}.".format(self.products_name.category.name, self.products_name.title)

    def get_absolute_url(self):
        return reverse('sale_laptop', kwargs={'slug': self.products_name.slug})


class RatingStar(models.Model):

    value = models.SmallIntegerField(verbose_name='Rating Star', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        ordering = ["-value"]


class Rating(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Star')
    laptop = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product laptop')
    total_ip_rating = models.SmallIntegerField(verbose_name='Total Rating Star', default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.star} - {self.laptop}"


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=14)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self):
        return "{} : {}.".format(self.title, self.author)


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_comment = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username


class PromoCode(models.Model):

    name = models.CharField(verbose_name='Name code', max_length=255)
    code = models.CharField(verbose_name='Promo code', primary_key=True, max_length=255)
    percent = models.DecimalField(verbose_name='Percent', max_digits=5, decimal_places=2, default=0)
    image_code = models.ImageField(verbose_name='Picture code', null=True, blank=True)

    def __str__(self):
        return self.code




