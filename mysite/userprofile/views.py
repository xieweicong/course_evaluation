from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm, get_activate_url, activate_user
from django.core.mail import send_mail
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from .models import Profile

# 用户主页
@login_required(login_url="/userprofile/login/")
def user_page(request):
    context = {"user": request.user}
    return render(request, "userprofile/mypage.html", context)


# 用户登录
def user_login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data["username"], password=data["password"])
            if get_object_or_404(User, username=data["username"]).is_active:
                if user:
                    # 将用户数据保存在 session 中，即实现了登录动作
                    login(request, user)
                    return redirect("userprofile:user_page")
                else:
                    return render(request, "userprofile/sendemail.html", {"content": "ユーザー名またパスワード入力間違い"})
            else:
                return render(request, "userprofile/sendemail.html", {"content": "メールで認証してください"})
        else:
            return render(request, "userprofile/sendemail.html", {"content": "ユーザー名またパスワード入力間違い"})
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        context = {"form": user_login_form}
        return render(request, "userprofile/login.html", context)
    else:
        return HttpResponse("GETとPOSTミス")


# 用户登出
def user_logout(request):
    logout(request)
    return redirect("/")


# 用户注册
def user_register(request):
    if request.method == "POST":
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            # 取出email和password
            user_name = request.POST["username"]
            number = request.POST["number"]
            email = number + "@gmail.com"
            # 实例化用户，然后赋值
            new_user = User()
            new_user.username = user_name
            new_user.email = email
            new_user.number = number
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data["password"])
            # 新建用户为非活跃用户，可通过验证变为活跃用户
            new_user.is_active = False
            new_user.save()
            new_user = User.objects.get(username=user_name)
            new_user.profile.number = number
            # 保存好数据后立即登录并返回博客列表页面
            # login(request, new_user)
            # 此处加入了邮箱验证的手段
            activate_url = get_activate_url(new_user)
            message = message_template + activate_url
            new_user.email_user(subject, message)
            return render(request, "userprofile/sendemail.html", {"content": "ご登録ありがとうございます。メールで認証してください"})
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == "GET":
        user_register_form = UserRegisterForm()
        context = {"form": user_register_form}
        return render(request, "userprofile/register.html", context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


class ActivateView(TemplateView):
    template_name = "userprofile/activate.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        # 認証トークンを検証して、
        result = activate_user(uidb64, token)
        # コンテクストのresultにTrue/Falseの結果を渡します。
        return super().get(request, result=result, **kwargs)

subject = "登録確認"
message_template = """
ご登録ありがとうございます。
以下URLをクリックして登録を完了してください。

"""