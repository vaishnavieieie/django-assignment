from django import forms
from .models import CustomerRequest

class CustomerRequestForm(forms.ModelForm):
    class Meta:
        model = CustomerRequest
        fields = ['request_type', 'request_details', 'attachment']
