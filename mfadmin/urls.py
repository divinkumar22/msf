# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
# from mfadmin.views import UserHome, UserLogin, otp_verfiy, deshborad, transactions, pickupmanHome, pickupLogin

from .views.user import UserHome, UserLogin, otp_verfiy, deshborad, transactions
from .views.pickupman import pickupmanHome, pickupLogin

urlpatterns = [
    # path('login/', login_view, name="login"),
    # path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('', UserHome.userHome, name='UserHome'),
    path('userLogin', UserLogin.UserLoginView, name='userLogin'),
    path("logout", LogoutView.as_view(), name="logout"),
    path('otp_verify/<int:pk>', otp_verfiy.Otp_verfiy, name='otp_verfiy'),
    path('dashboard', deshborad.DeshboradVeiw, name='deshborad'),
    path('transactions', transactions.TranactionVeiw, name='transactions'),
    path('PickupMan', pickupmanHome.pickupmanHome, name='pickupman'),
    path('pickupmanlogin', pickupLogin.pickupLoginView, name='pickupmanlogin'),

]
