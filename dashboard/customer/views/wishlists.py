from django.views.generic import DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from dashboard.customer.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.exceptions import FieldError
from product.models import WishlistProductModel


class CustomerWishlistListView(LoginRequiredMixin, HasCustomerAccessPermission, ListView):
    template_name = "dashboard/customer/wishlists/wishlist-list.html"
 

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = WishlistProductModel.objects.filter(user=self.request.user)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset


class CustomerWishlistDeleteView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, DeleteView):
    http_method_names = ["post"]
    success_url = reverse_lazy('dashboard:customer:wishlist-list')
    success_message = "محصول با موفقیت از لیست حذف شد"

    def get_queryset(self):
        return WishlistProductModel.objects.filter(user=self.request.user)