from django.views.generic import TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from dashboard.customer.forms import CustomerPasswordChangeForm,CustomerProfileEditForm
from django.urls import reverse_lazy
from accounts.models import Profile
class CustomerDashboardHomeView(LoginRequiredMixin, HasCustomerAccessPermission, TemplateView):
    template_name = "dashboard/customer/home.html"

class CustomerSecurityEditView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = "dashboard/customer/profile/security-edit.html"
    form_class = CustomerPasswordChangeForm
    success_url = reverse_lazy("dashboard:customer:security-edit")
    success_message = "بروز رسانی پسورد با موفقیت انجام شد"

class CustomerProfileEditView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/customer/profile/profile-edit.html"
    form_class = CustomerProfileEditForm
    success_url = reverse_lazy("dashboard:customer:profile-edit")
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)