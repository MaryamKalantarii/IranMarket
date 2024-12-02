from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    FormView,
    View,
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from order.permissions import HasCustomerAccessPermission
from order.models import *
from order.forms import CheckOutForm
from cart.models import *
from django.urls import reverse_lazy
from cart.cart import CartSession
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import redirect
from payment.zarinpal_client import ZarinPalSandbox
from payment.models import PaymentModel


class OrderCheckOutView(LoginRequiredMixin, HasCustomerAccessPermission, FormView):
    template_name = "order/checkout.html"
    form_class = CheckOutForm
    success_url = reverse_lazy('order:completed')

    def get_form_kwargs(self):
        kwargs = super(OrderCheckOutView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        cleaned_data = form.cleaned_data
        address = cleaned_data['address_id']
        coupon = cleaned_data['coupon']

        cart = CartModel.objects.get(user=user)
        order = self.create_order(address)

        self.create_order_items(order, cart)
        self.clear_cart(cart)

        total_price = order.calculate_total_price()
        self.apply_coupon(coupon, order, user, total_price)
        order.save()
        # zarinpal = ZarinPalSandbox()

        # # ارسال درخواست پرداخت
        # response = zarinpal.payment_request(order.total_price)

        # # بررسی پاسخ و استخراج authority
        # print(response)  # Debugging
        # authority = response.get('data', {}).get('authority')
        # if not authority:
        #     raise ValueError("Authority key is missing in the response.")

        # # تولید لینک پرداخت
        # payment_url = zarinpal.generate_payment_url(authority)

        # هدایت کاربر به درگاه پرداخت
        return redirect(self.create_payment_url(order))



    def create_payment_url(self, order):
        zarinpal = ZarinPalSandbox()
        response = zarinpal.payment_request(order.get_price())
      
        payment_obj = PaymentModel.objects.create(
            authority_id = response.get('data', {}).get('authority'),
            amount=order.get_price(),
        )
        order.payment = payment_obj
        order.save()
        return zarinpal.generate_payment_url(response.get('data', {}).get('authority'))

    def create_order(self, address):
        return OrderModel.objects.create(
            user=self.request.user,
            address=address.address,
            state=address.state,
            city=address.city,
            zip_code=address.zip_code,
        )

    def create_order_items(self, order, cart):
        for item in cart.cart_items.all():
            OrderItemModel.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.get_price(),
            )

    def clear_cart(self, cart):
        cart.cart_items.all().delete()
        CartSession(self.request.session).clear()

    def apply_coupon(self, coupon, order, user, total_price):
        if coupon:
        #     discount_amount = round(
        #         (total_price * Decimal(coupon.discount_percent / 100)))
        #     total_price -= discount_amount

            order.coupon = coupon
            coupon.used_by.add(user)
            coupon.save()

        order.total_price = total_price

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModel.objects.get(user=self.request.user)
        context["addresses"] = UserAddressModel.objects.filter(
            user=self.request.user)
        total_price = cart.calculate_total_price()
        context["total_price"] = total_price
        context["shipping_price"] = round(total_price + 40000)
        return context

class ValidateCouponView(LoginRequiredMixin, HasCustomerAccessPermission, View):

    def post(self, request, *args, **kwargs):
        code = request.POST.get("code")
        user = self.request.user

        status_code = 200
        message = "کد تخفیف با موفقیت ثبت شد"
        total_price = 0
        shipping_price = 0

        try:
            coupon = CouponModel.objects.get(code=code)
        except CouponModel.DoesNotExist:
            return JsonResponse({"message": "کد تخفیف یافت نشد"}, status=404)
        else:
            if coupon.used_by.count() >= coupon.max_limit_usage:
                status_code, message = 403, "محدودیت در تعداد استفاده"

            elif coupon.expiration_date and coupon.expiration_date < timezone.now():
                status_code, message = 403, "کد تخفیف منقضی شده است"

            elif user in coupon.used_by.all():
                status_code, message = 403, "این کد تخفیف قبلا توسط شما استفاده شده است"

            else:
                cart = CartModel.objects.get(user=self.request.user)

                total_price = cart.calculate_total_price()
                total_price = round(
                    total_price - (total_price * (coupon.discount_percent/100)))
                shipping_price = round(total_price + 40000)
        return JsonResponse({"message": message, "shipping_price": shipping_price, "total_price": total_price}, status=status_code)




class OrderCompletedView(LoginRequiredMixin, HasCustomerAccessPermission, TemplateView):
    template_name = "order/completed.html"

class OrderFailedView(LoginRequiredMixin, HasCustomerAccessPermission, TemplateView):
    template_name = "order/failed.html"
