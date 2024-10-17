from .models import Account
from .models import ProfileImage, BackgroundImage, Bio
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        ProfileImage.objects.create(user=instance)
        BackgroundImage.objects.create(user=instance)
        Bio.objects.create(user=instance)

        

