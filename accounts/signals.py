
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
from .models import UserProfile 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_profile_receiver(sender, instance, created, *args, **kwargs):
    # print(created)
    if created:
        # print('profile created')
        UserProfile.objects.create(user=instance)
        # print(f"Profile created for {instance.email}")
    else:
        # print('profile not created')
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            # print('profile updated')
        except:
            # print('profile not updated')
            UserProfile.objects.create(user=instance)
            # print(f"Profile created for {instance.email}")




@receiver(pre_save, sender=settings.AUTH_USER_MODEL)
def pre_save_profile_receiver(sender, instance, *args, **kwargs):
    print(f"{instance.email} is being saved")