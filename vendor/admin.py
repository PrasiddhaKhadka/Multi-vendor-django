from django.contrib import admin
from . models import Vendor
# from  utils.email_utils import send_vendor_approval_notification    
# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name', 'is_approved','created_at',)
    list_display_links = ('vendor_name', 'is_approved','created_at',) 
    list_filter = ['is_approved', 'created_at']
    search_fields = ['vendor_name', 'vendor_user__email']
    readonly_fields = ['created_at', 'modified_at']

    # actions = ['approve_vendors', 'reject_vendors']

    # def approve_vendors(self, request, queryset):
    #     """Custom admin action to approve vendors"""
    #     updated = 0
    #     for vendor in queryset.filter(is_approved=False):
    #         vendor.is_approved = True
    #         vendor.save()
    #         send_vendor_approval_notification(vendor, approved=True)
    #         updated += 1
        
    #     self.message_user(request, f'{updated} vendors were approved and notified.')
    # approve_vendors.short_description = "Approve selected vendors"
    
    # def reject_vendors(self, request, queryset):
    #     """Custom admin action to reject vendors"""
    #     updated = 0
    #     for vendor in queryset.filter(is_approved=True):
    #         vendor.is_approved = False
    #         vendor.save()
    #         send_vendor_approval_notification(vendor, approved=False)
    #         updated += 1
        
    #     self.message_user(request, f'{updated} vendors were rejected and notified.')
    # reject_vendors.short_description = "Reject selected vendors"