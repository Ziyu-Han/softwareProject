from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from random import choice

# Create your views here.


def root(request):
    return render(request, 'root.html')


def toLogin_view(request):
    return render(request, 'login.html')


def login_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')

    if u and p:
        if UserInfo.objects.filter(username=u, userpwd=p).count() >= 1:
            return HttpResponse("登陆成功")
        return HttpResponse("用户名或密码错误")
    return HttpResponse("error")


def toRegister_view(request):
    return render(request, 'register.html')


def register_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')

    if u and p:
        if UserInfo.objects.filter(username=u).count():
            return HttpResponse("该用户名已注册！")
        user = UserInfo(userid=choice(range(1000, 10000)), username=u, userpwd=p)
        user.save()
        return HttpResponse("注册成功！")

    return HttpResponse("用户名或密码为空！")


def zdx_view(request):
    return render(request, 'zdx_info.html')


def xs_view(request):
    return render(request, 'xs_info.html')


def xy_view(request):
    return render(request, 'xy_info.html')


def xz_view(request):
    return render(request, 'xz_info.html')


def zdx_review_view(request):
    return render(request, 'xz_review.html')


def xs_review_view(request):
    return render(request, 'xz_review.html')


def xy_review_view(request):
    return render(request, 'xz_review.html')


def xz_review_view(request):
    return render(request, 'xz_review.html')


def xz_review_view(request):
    return render(request, 'xz_review.html')


    # if u == 'han' and p == '1234':
    #     return HttpResponse("success")
    # else:
    #     return HttpResponse("fail")

    # return render(request, 'login.html')

