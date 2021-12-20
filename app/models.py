from django.db import models
from django.core.validators import RegexValidator
import re
from django.db.models.fields import BooleanField, CharField
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'

        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email Address already in use'

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'

        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'

        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        
        if form['adminKey'] != 'DragonsEdge&HoneyBee':
            errors['adminKey'] = 'Please get the right Key'

        return errors

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)
    adminKey = models.CharField(max_length=255)

    objects = UserManager()

    userCreatedAt = models.DateTimeField(auto_now_add=True)
    userUpdatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

class Profile(models.Model):
    image = models.ImageField(upload_to='profileImgs', default='default.jpg')
    user = models.OneToOneField(User, unique=True, on_delete=CASCADE)
    def __str__(self):
        return f'{self.user.username} Profile'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)

class CustomerManager(models.Manager):
    def validate(self, form):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'

        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email Address already in use'

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'

        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'

        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'

        return errors

class Customer(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)

    objects = CustomerManager()

    customerCreatedAt = models.DateTimeField(auto_now_add=True)
    customerUpdatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

class Account(models.Model):
    image = models.ImageField(upload_to='customerImgs', default='default.jpg')
    customer = models.OneToOneField(Customer, unique=True, on_delete=CASCADE)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zipCode = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f'{self.customer.username} Account'

def create_customer_account(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(customer=instance)
        post_save.connect(create_customer_account, sender=Customer)

class Event(models.Model):
    eventName = models.CharField(max_length=255)
    date = models.DateTimeField()
    details = models.TextField()
    location = models.CharField(max_length=255)
    eventStatus = models.BooleanField(default=0)
    def getDate(self):
        return self.date.date()

class Format(models.Model):
    medium = models.CharField(max_length=255)

class Language(models.Model):
    lang = models.CharField(max_length=255)

class Product(models.Model):
    prodName = models.CharField(max_length=255)
    prodDetails = models.TextField()
    author = models.CharField(max_length=255, blank=True)
    illustrator = models.CharField(max_length=255, blank=True)
    isbn = models.CharField(max_length=255, blank=True)
    quantity = models.IntegerField(default=1, blank=True)
    prodPrice = models.CharField(max_length=255, blank=True, default='TBD')
    prodType = models.BooleanField(default=0)
    prodMedium = models.ForeignKey(Format, related_name='theMedium', on_delete=CASCADE, blank=True)
    prodLang = models.ForeignKey(Language, related_name='theLang', on_delete=CASCADE, blank=True)
    def __str__(self):
        return self.prodName

class Picture(models.Model):
    imageName = models.CharField(max_length=255, blank=True)
    prodimg = models.ImageField(upload_to='prodImages', default='default.jpg')
    product = models.OneToOneField(Product, unique=True, on_delete=CASCADE)
    def __str__(self) -> str:
        return f'{self.product.prodName} Picture'

def create_product_picture(sender, instance, created, **kwargs):
    if created:
        Product.objects.create(product.instance)
        post_save.connect(create_product_picture, sender=Product)
