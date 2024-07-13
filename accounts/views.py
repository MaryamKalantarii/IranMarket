from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
# from .forms import Loginform


# class LoginView(FormView):
#     template_name = 'registration/login-register.html'
#     form_class = Loginform
#     success_url = '/'
#     def form_valid(self, form):
#         phone = self.request.POST.get('phone')
#         user = authenticates(phone=phone)
#         if user is not None:
#             login(self.request, user)
#             return super().form_valid(form)




# from django.views.generic import TemplateView

# # Create your views here.

# class LoginView(TemplateView):
#     template_name = 'registration/login-register.html'













# from django.views import View
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.conf import settings
# import random
# import re
# from .forms import ContactForm

# class ContactView(View):
#     form_class = ContactForm
#     template_name = 'contact.html'

#     def get(self, request):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             contact = form.cleaned_data['contact']
#             if self.is_valid_email(contact):
#                 code = self.generate_verification_code()
#                 self.send_verification_email(contact, code)
#             elif self.is_valid_phone(contact):
#                 code = self.generate_verification_code()
#                 self.send_verification_sms(contact, code)
#             else:
#                 form.add_error('contact', 'ورودی شما باید یک ایمیل معتبر یا شماره تلفن باشد.')
#                 return render(request, self.template_name, {'form': form})

#             return redirect('success')
#         return render(request, self.template_name, {'form': form})

#     def is_valid_email(self, contact):
#         return re.match(r"[^@]+@[^@]+\.[^@]+", contact)

#     def is_valid_phone(self, contact):
#         return re.match(r"^\+?1?\d{9,15}$", contact)

#     def generate_verification_code(self):
#         return random.randint(1000, 9999)

#     def send_verification_email(self, email, code):
#         subject = 'کد تأیید شما'
#         message = f'کد تأیید شما: {code}'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email]
#         send_mail(subject, message, email_from, recipient_list)

#     def send_verification_sms(self, phone, code):
#         # استفاده از سرویس ارسال SMS برای ارسال کد تأیید
#         pass
