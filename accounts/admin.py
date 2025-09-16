from django.contrib import admin
from .models import User, UserProfile

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role','is_active')
    readonly_fields = ('date_joined', 'last_login','password',)
    ordering = ('-date_joined',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address_line_1', 'address_line_2', 'country', 'state', 'city')