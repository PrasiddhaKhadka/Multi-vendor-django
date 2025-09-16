from django.contrib import admin
from . models import Vendor
# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name', 'is_approved','created_at',)
    list_display_links = ('vendor_name', 'is_approved','created_at',)