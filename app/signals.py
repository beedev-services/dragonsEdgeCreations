from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Product)
def create_picture(sender, instance, created, **kwargs):
    if created:
        Picture.objects.create(product=instance)

@receiver(post_save, sender=Product)
def save_picture(sender, instance, **kwargs):
    instance.picture.save()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Customer)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(customer=instance)

@receiver(post_save, sender=Customer)
def save_account(sender, instance, **kwargs):
    instance.account.save()