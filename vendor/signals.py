from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vendor

# Signal to notify admin when vendor registers
@receiver(post_save, sender=Vendor)
# instance is acutally the object of vendor 
# vendor = Vendor(
#     vendor_name="ShopX",
#     is_approved=False,
#     vendor_user=user,
#     vendor_profile=profile

# )

def vendor_register_notification_to_admin(sender, instance, created, *args, **kwargs):
    if created:
        from utils.email_utils import send_vendor_registration_notification_to_admin
        send_vendor_registration_notification_to_admin(instance)
    else:
        if not created:
            # Check if is_approved field has changed
            if instance.tracker.has_changed('is_approved') and instance.is_approved:
                # Import here to avoid circular imports
                from utils.email_utils import send_vendor_approval_notification
                send_vendor_approval_notification(instance, approved=True)



# Duplication of Code

# @receiver(post_save, sender=Vendor)
# def vendor_register_notification_to_customer(sender, instance, created, *args, **kwargs):
#     if not created:
#         # Check if is_approved field has changed
#         if instance.tracker.has_changed('is_approved') and instance.is_approved:
#             # Import here to avoid circular imports
#             from utils.email_utils import send_vendor_approval_notification
#             send_vendor_approval_notification(instance, approved=True)