from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Product)
def createUpload(sender, instance, created, **kwargs):
    if created:
        Prodimg.objects.create(Product.instance)

@receiver(post_save, sender=Product)
def saveUpload(sender, instance, **kwargs):
    instance.prodimg.save()