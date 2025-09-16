
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
from .models import User,UserProfile 
from vendor.models import Vendor

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_profile_receiver(sender, instance, created, *args, **kwargs):
    # print(created)
    if created:
        # --> 😁😁😁😁😁 CREATING USERPROFILE FOR EVERY NEW USER 😁😁😁😁😁 <--
        # print('profile created')
        UserProfile.objects.create(user=instance)
        # print(f"Profile created for {instance.email}")


        # --> 😁😁😁😁😁 CREATING VENDOR OR CUSTOMER ACCORDING TO ROLE 😁😁😁😁😁 <--
        if instance.role == User.RESTAURANT:
            Vendor.objects.create(
                                  vendor_user=instance,
                                  vendor_name=instance.email.split("@")[0],
                                  vendor_profile = instance.userprofile
                                  )
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