from django.db import models
from django.contrib.auth.models import User

class CustomerRequest(models.Model):
    status_options = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    request_options = [
        ('general', 'General'),
        ('technical', 'Technical'),
        ('billing', 'Billing'),
        ('servicing', 'Servicing'),
        ('other', 'Other'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=request_options)
    request_details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    request_status = models.CharField(max_length=20, choices=status_options, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - {self.customer.username}"

    class Meta:
        permissions = [
            ('can_view_requests', 'Can view support requests'),
            ('can_change_status', 'Can change request status'),
        ]
