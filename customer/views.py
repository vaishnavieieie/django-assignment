from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomerRequest
from .forms import CustomerRequestForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = CustomerRequestForm()
    return render(request, 'submit_request.html', {'form': form})

@login_required
def request_list(request):
    requests = CustomerRequest.objects.filter(customer=request.user)
    return render(request, 'request_list.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(CustomerRequest, pk=pk, customer=request.user)
    return render(request, 'request_detail.html', {'service_request': service_request})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import CustomerRequest

@login_required
@permission_required('service.can_view_requests', raise_exception=True)
def support_request_list(request):
    # Fetch all customer requests
    requests = CustomerRequest.objects.all()
    return render(request, 'support_list_all.html', {'requests': requests})


@login_required
@permission_required('service.can_change_status', raise_exception=True)
def update_status(request, pk):
    customer_request = get_object_or_404(CustomerRequest, pk=pk)

    if request.method == 'POST':
        # Update the status
        new_status = request.POST.get('request_status')
        if new_status in dict(CustomerRequest.status_options):
            customer_request.request_status = new_status
            if new_status == 'resolved':
                from django.utils.timezone import now
                customer_request.resolved_at = now()
            customer_request.save()
            messages.success(request, 'Request status updated successfully.')
        else:
            messages.error(request, 'Invalid status.')

        return redirect('support_request_list')

    return render(request, 'update_status.html', {'customer_request': customer_request})

# view account details
@login_required
def account_details(request):
    return render(request, 'account_details.html')
    