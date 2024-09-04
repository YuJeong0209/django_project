# blog/urls.py

from django.urls import path
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분

    path('login/', views.login),
  
]


