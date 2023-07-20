from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import RegisterForm, LoginForm

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
            return redirect('/')
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