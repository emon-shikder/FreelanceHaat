from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html

User = get_user_model()

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'first_name', 'last_name', 'is_active', 'profile_picture_preview', 'hourly_rate')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('user_type', 'is_active')
    ordering = ['username']
    
    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;">', obj.profile_picture.url)
        return "No image"
    profile_picture_preview.short_description = 'Profile Picture'

admin.site.register(User, CustomUserAdmin)
