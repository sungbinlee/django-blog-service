from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import RegisterForm, LoginForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# 이메일관련
import ssl
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.conf import settings
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



# Create your views here.
# user 관련된 기능
# 회원가입
# 로그인
# 로그아웃


# Registration
class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        # 회원가입 페이지
        # 정보를 입력할 폼을 보여주어야 한다.
        form = RegisterForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 로그인한 다음 이동
            current_site = get_current_site(request)
            mail_subject = 'Email Verification'
            message = render_to_string(
                'user/email_verification.html',
                {
                    'user': user,
                    'domain': 'sungbinlee.dev',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                    'protocol': 'https' if request.is_secure() else 'http',
                },
            )
            
            send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email], html_message=message)

            return redirect('user:verification_sent')

        else:
            context = {
                'form': form,
                'title': 'User'
            }
            return render(request, 'user/register.html', context)


# Login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        
        form = LoginForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password) # True, False
            
            if user:
                login(request, user)
                return redirect('/')
            
        # form.add_error(None, '아이디가 없습니다.')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/login.html', context)


### Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')
    

class ProfileUpdateView(LoginRequiredMixin, View):
    template_name = 'user/profile_update.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('/')  # Redirect back to the same page after updating
        
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    

User = get_user_model()


class VerifyEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('user:login')
        else:
            return render(request, 'index.html', {'error' : '계정 활성화 오류'})



class VerificationSentView(View):
    def get(self, request):
        return render(request, 'user/verification_sent.html')
