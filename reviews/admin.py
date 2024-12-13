from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('job', 'reviewer', 'reviewed', 'rating', 'created_at')
    search_fields = ('job__title', 'reviewer__username', 'reviewed__username', 'rating')
    list_filter = ('rating', 'created_at')
    ordering = ['-created_at']

admin.site.register(Review, ReviewAdmin)
