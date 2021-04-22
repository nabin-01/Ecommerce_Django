from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse
from django.utils import timezone
STATUS = (('active', 'active'), ('passive', 'passive'))
PRODUCT_LABEL = (('hot', 'hot'), ('new', 'new'), ('most_viewed', 'most_viewed'), ('', 'default'))


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS, default='active')

    def __str__(self):
        return self.title

    def get_cat_url(self):
        return reverse('myapp:category', kwargs={'slug': self.slug})


class Slider(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/')
    status = models.CharField(max_length=100, choices=STATUS, default='active')

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/')
    status = models.CharField(max_length=100, choices=STATUS, default='active')
    rank = models.IntegerField(unique=True)

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    status = models.CharField(max_length=100, choices=STATUS, default='active')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    slug = models.CharField(unique=True, max_length=100)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    discount = models.IntegerField(null=True, default=0)
    status = models.CharField(max_length=100, choices=STATUS, default='active')
    label = models.CharField(max_length=100, choices=PRODUCT_LABEL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)
    specification = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_product_url(self):
        return reverse('myapp:products', kwargs={'slug': self.slug})

    def get_cart_url(self):
        return reverse('myapp:cart', kwargs={'slug': self.slug})


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100, help_text='please provide relevant topic!')
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SiteReview(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, help_text='you can specify your permanent job!')
    review = models.TextField()
    email = models.EmailField(default=None)
    status = models.CharField(max_length=100, choices=STATUS, default='active')
    image = models.ImageField(upload_to='media/')
    date_added = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)],
                                 help_text='enter rating between 1-5!')

    def __str__(self):
        return self.name


class Review(models.Model):
    username = models.CharField(max_length=200, blank=True)
    review = models.TextField()
    email = models.EmailField(max_length=200, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100, choices=STATUS, default='active')
    slug = models.CharField(max_length=100)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)],
                                 help_text='enter rating between 1-5!')

    def __str__(self):
        return self.username


class Cart(models.Model):
    username = models.CharField(max_length=200, default=None)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total = models.IntegerField()
    checkout = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=STATUS, default='active')

    def __str__(self):
        return self.username


class CartTotal(models.Model):
    username = models.CharField(max_length=200, default=None)
    net_total = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=None)
    slug = models.CharField(max_length=100, unique=True, default=None)
    shipping_cost = models.IntegerField(default=0)
    grand_total = models.IntegerField(default=0)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Checkout(models.Model):
    username = models.CharField(max_length=200, default=None)
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=200, default=None)
    email = models.EmailField()
    shipping_add = models.CharField(max_length=200)
    mobile_no = models.IntegerField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    checkout = models.BooleanField(default=True)
    date_checked = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name



