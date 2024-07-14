from django.shortcuts import redirect
from django.views.generic import FormView, CreateView
from .forms import CustomUserCreation

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreation
    success_url = '/accounts/login/' #'registration/login'

    def delete_code(self):
        time.sleep(10)
        self.request.session.pop('code')
        self.request.session.save()

    def form_valid(self, form):
        form.save()
        code = random.randint(1000,1000)
        self.request.session['code'] = code
        print(self.request.session.get('code'))
        tr1 = threading.Thread(target=self.delete_code)
        tr1.start()
        return redirect("accounts:otp-verify")    
    def form_invalid(self, form):
        pass
       
























# class LoginView(FormView):
#     template_name = 'registration/login-register.html'
#     form_class = SignUpForm
#     success_url = '/accounts/signup/'
#     def form_valid(self, form):
#         email = self.request.POST.get('email')
#         user = authenticate(email=email)
#         if user is not None:
#             login(self.request, user)
#             return super().form_valid(form)


# class SignupView(CreateView):
#     template_name ='registration/login.html'
#     form_class = CustomeUserCreation
#     success_url = '/'

#     def form_valid(self, form):
#         form.seve()
#         email = self.request.POST.get('email')
#         password = self.request.POST.get('password1')
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             login(self.request, user)
#             return super().form_valid(form)

#     def form_invalid(self, form):
#         messages.add_message(self.request, messages.ERROR, 'Invalid Credentials')
#         return super().form_invalid(form)












