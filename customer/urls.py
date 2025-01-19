from django.urls import path
from . import views

urlpatterns = [
    # customer side
    path('submit/', views.submit_request, name='submit_request'),
    path('requests/', views.request_list, name='request_list'),
    path('requests/<int:pk>/', views.request_detail, name='request_detail'),
    # support side
    path('support/requests/', views.support_request_list, name='support_request_list'),
    path('support/update_status/<int:pk>/', views.update_status, name='update_status'),
    # view account details
    path('account/', views.account_details, name='account_details'),
]
