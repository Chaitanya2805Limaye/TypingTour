from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/register',views.register_page,name='register'),
    path('/login',views.login_page, name='login'),
    path('/leaderboard',views.leaderboard, name='leaderboard'),
]
