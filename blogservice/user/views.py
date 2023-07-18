from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import RegisterForm

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