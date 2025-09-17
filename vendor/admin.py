from django.contrib import admin
from . models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name', 'is_approved','created_at',)
    list_display_links = ('vendor_name', 'is_approved','created_at',) 
    list_filter = ['is_approved', 'created_at']
    search_fields = ['vendor_name', 'vendor_user__email']
    readonly_fields = ['created_at', 'modified_at']
