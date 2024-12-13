from django.contrib import admin
from .models import Job
from .models import Proposal

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'budget', 'created_at', 'status', 'deadline')
    search_fields = ('title', 'client__username', 'status')
    list_filter = ('status', 'created_at')
    ordering = ['-created_at']

admin.site.register(Job, JobAdmin)

class ProposalAdmin(admin.ModelAdmin):
    list_display = ('job', 'freelancer', 'bid_amount', 'created_at', 'accepted')
    search_fields = ('job__title', 'freelancer__username', 'accepted')
    list_filter = ('accepted', 'created_at')
    ordering = ['-created_at']

admin.site.register(Proposal, ProposalAdmin)