from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomeUser,Profail


@receiver(post_save, sender=CustomeUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profail.objects.create(user=instance)