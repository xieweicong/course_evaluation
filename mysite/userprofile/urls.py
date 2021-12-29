from django.urls import path
from . import views

app_name = "userprofile"

urlpatterns = [
    # 用户页面
    path("user_page/", views.user_page, name="user_page"),
    # 用户登录
    path("login/", views.user_login, name="login"),
    # 用户退出
    path("logout/", views.user_logout, name="logout"),
    # 用户注册
    path("register/", views.user_register, name="register"),
    # 邮箱验证
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
]
