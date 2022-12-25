
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from mfadmin.models import NormalUser,User


def UserLoginView(request):
    msg = None
    if request.method == 'POST':
        username = request.POST.get("account_no")
        password = request.POST.get("password")
        if request.user.is_authenticated:
            return redirect("/adminuser/userHome")
        user = User.objects.filter(username=username).first()
        if user is not None and user.is_admin:
            if user.check_password(password):
                login(request, user)
                return redirect("/adminuser/userHome")
            else:
                msg = "incorrect password"
        else:
            msg = 'Invalid credentials'
    return render(request, "user_login.html", {"msg": msg})


