from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, TemplateView,UpdateView,ListView,DetailView
from .forms import *
import time
import random
import threading
from django.core.exceptions import ObjectDoesNotExist
import uuid
from accounts.api.V1.multi_threading import SendEmailWithThreading
from mail_templated import EmailMessage
from .models import CustomeUser,Profail
from django.contrib.auth import login ,password_validation,logout,authenticate
from django.contrib import messages
from django.shortcuts import get_object_or_404




class OtpVerifyView(FormView):
    template_name = "registration/otp.html"
    form_class = OtpForm
    success_url = "/accounts/signup/"

    def form_valid(self, form):
        try:
            code = self.request.POST['otp_code']
            if (self.request.session.get('code')) and (int(code) == self.request.session['code']):
                return redirect("accounts:signup")
            else:
                print(self.request.session.get('code'))
                return redirect(self.request.path_info)
        except:
            return render(self.request, 'registration/otp.html')
    

class LoginView(FormView):
    template_name = 'registration/login-register.html'
    form_class = LoginForm
    success_url = '/'
    
    def delete_code(self):
        time.sleep(15)
        self.request.session.pop('code')
        self.request.session.save()

    def form_valid(self, form):
        global redirection, email
        try : 
            user = CustomeUser.objects.get(email=self.request.POST.get('email'))
            assert user.password != ""
            redirection = 0
        except AssertionError:
            redirection = 1
        except ObjectDoesNotExist:
            redirection = 1
            user = CustomeUser.objects.create(email=self.request.POST.get('email'), username = uuid.uuid4() )

        email = form.cleaned_data['email']
        code = random.randint(1000, 10000)
        self.request.session['code'] = code
        print(self.request.session.get('code'))
        tr1 = threading.Thread(target=self.delete_code)
        tr1.start()
        # message = EmailMessage("email/email2.html",{"code":code},"maryam@admin.com",to=[user.email],)
        # email = SendEmailWithThreading(message)
        # email.start()
        return redirect("accounts:otp-verify")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'دوباره ایمیل خود را وارد کنید')
        return super().form_invalid(form)
    

def signup(request):
    user = CustomeUser.objects.get(email=email)
    if redirection == 0:
        login(request, user)
        return redirect("root:home")
    else:
        form = CustomUserCreation()
        context = {
                'form': form,
            }
        if request.method == "GET" : 
            return render(request, 'registration/login.html', context=context)
        elif request.method == "POST" :
            form = CustomUserCreation(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 == password2:
                    user.username = username
                    password_validation.validate_password(password1)
                    user.set_password(password1)
                    user.save()
                    login(request, user)
                    return redirect('root:home')

            else:
                messages.add_message(request, messages.ERROR, 'لطفا رمز عبور یا نام کاربری را درست وارد کنید')
                return redirect(request.path_info)

        return render(request, 'registration/login.html', context=context)


class Logout(TemplateView):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")
    

class Login_password(FormView):
    template_name = 'registration/login-password.html'
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        
        messages.add_message(self.request, messages.ERROR, 'ایمیل یا رمز عبور اشتباه است')
        return super().form_invalid(form)



def profile_Edit(request,pk):

    if request.method == 'GET':
        form = Profile_Form()
        user = request.user
        profile = get_object_or_404(Profail, user=user)
        context = {
            'form':form,
            'profile': profile
        }
        return render (request,'profile/profile-personal-info.html',context=context)
    elif request.method == 'POST':
        profile = Profail.objects.get(user=pk)
        form = Profile_Form(request.POST,request.FILES ,instance=profile)
        if form.is_valid():
            form.save()
            request.user.is_verified = True
            request.user.save()
            return redirect('root:home')
        else:
            return render (request,'profile/profile-personal-info.html',{'form':form})



class Profile_View(DetailView):
    model = Profail
    template_name = 'profile/profile.html'
    context_object_name = 'profile'

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(Profail, user=user)
        context = {
            'profile': profile
        }
        
        return render(request,'profile/profile.html',context=context)
        