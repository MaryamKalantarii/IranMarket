from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView,CreateView,UpdateView
from .forms import Loginform,CustomeUserCreation
from django.contrib import messages


class LoginView(FormView):
    template_name = 'registration/login-register.html'
    form_class = Loginform
    success_url = 'registration/login.html'
    def form_valid(self, form):
        phone = self.request.POST.get('phone')
        user = authenticates(phone=phone)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)


class SignupView(CreateView):
    template_name ='registration/login.html'
    form_class = CustomeUserCreation
    success_url = '/'

    def form_valid(self, form):
        form.seve()
        email = self.request.POST.get('email')
        password = self.request.POST.get('password1')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Invalid Credentials')
        return super().form_invalid(form)












