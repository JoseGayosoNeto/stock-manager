from django.db.models.signals import post_save
from django.dispatch import receiver
from inflows.models import Inflow


@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    # created = True -> Create new registry post
    # created = False -> Update registry post
    # This signals is designed to only work in new registry posts
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity += instance.quantity
            product.save()
