from django.contrib import admin
from .models import CustomerRequest

@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ('request_type', 'customer', 'request_status', 'submitted_at', 'resolved_at')
    list_filter = ('request_status',)
    search_fields = ('request_type', 'request_details', 'customer__username')
