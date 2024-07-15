from django.shortcuts import redirect
from django.views.generic import FormView, CreateView
from .forms import CustomUserCreation,OtpForm
from django.views.generic import TemplateView
import time
import random
import threading
# Create your views here.

class LoginView(TemplateView):
    template_name = 'registration/login.html'






class SignUpView(CreateView):
    template_name = 'registration/login-register.html'
    form_class = CustomUserCreation
    success_url = '/accounts/login/' #'registration/login'

    def delete_code(self):
        time.sleep(15)
        self.request.session.pop('code')
        self.request.session.save()

    def form_valid(self, form):
        user = form.save()
        code = random.randint(1000, 10000)
        self.request.session['code'] = code
        print(self.request.session.get('code'))
        tr1 = threading.Thread(target=self.delete_code)
        tr1.start()
        return redirect("accounts:otp-verify")

    def form_invalid(self, form):
        return redirect(self.request.path_info)
       





class OtpVerifyView(FormView):
    template_name = "registration/otp.html"
    form_class = OtpForm
    success_url = "/"

    def form_valid(self, form):
        code = self.request.POST['otp_code']
        if (self.request.session.get('code')) and (int(code) == self.request.session['code']):
            return redirect('/')
        else:
            print(self.request.session.get('code'))
            return redirect(self.request.path_info)




















