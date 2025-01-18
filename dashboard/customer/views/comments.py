from django.views.generic import ListView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.core.exceptions import FieldError
from review.models import ReviewModel
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class CommentListView(LoginRequiredMixin, HasCustomerAccessPermission, ListView):
    template_name = "dashboard/customer/comments/comments.html"

    def get_queryset(self):
        queryset = ReviewModel.objects.filter(user=self.request.user)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset

class CommentDeleteView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, DeleteView):
    http_method_names = ["post"]
    success_url = reverse_lazy('dashboard:customer:comment-list')
    success_message = "نظر شما با موفقیت حذف شد"

    def get_queryset(self):
        return ReviewModel.objects.filter(user=self.request.user)