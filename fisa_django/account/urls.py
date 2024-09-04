from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('login/', views.user_login), #localhost:8000/account/login

    #로그아웃, 로그인 장고의 view 기능 추가, templates/registration/디렉토리와 연동됨
    path('login/', auth_views.LoginView.as_view()),
    path('', auth_views.LogoutView.as_view()) #주소로 접근해서 콘솔에 405가 뜨는 것을 확인
]