from django.db import models
from django.conf import settings
from accounts.models import UserProfile

# Create your models here.
class Vendor(models.Model):
    vendor_user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='vendor',  on_delete=models.CASCADE)
    vendor_profile = models.OneToOneField(UserProfile, related_name='vendor_profile', on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=50)
    vendor_license = models.ImageField(upload_to='media/vendor/license')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.vendor_name