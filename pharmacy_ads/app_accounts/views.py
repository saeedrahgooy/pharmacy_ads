from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import OTP, UserProfile
from app_requests.models import Request
from app_ads.models import Ad

import random


def login_otp(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        code = str(random.randint(100000, 999999))

        OTP.objects.create(phone=phone, code=code)

        print("OTP:", code)  # فعلاً برای تست

        request.session["phone"] = phone
        return redirect("verify_otp")

    return render(request, "accounts/login_otp.html")



def verify_otp(request):
    phone = request.session.get('phone')
    if request.method == "POST":
        code = request.POST.get('code')
        otp = OTP.objects.filter(phone=phone, code=code)
        if otp:
            user, created = User.objects.get_or_create(username=phone)
            profile, _ = UserProfile.objects.get_or_create(user=user, phone=phone)
            login(request, user)
            if profile.role is None:
                return redirect("choose_role")
            return redirect('ads:list')
    return render(request, "accounts/verify_otp.html")


def choose_role(request):
    if request.method == "POST":
        role = request.POST.get('role')
        profile  = request.user.userprofile
        profile.role = role
        profile.save()
        return redirect("ads:list")
    return render(request, "accounts/choose_role.html")


def logout_view(requset):
    logout(requset)
    return redirect("login_otp")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login_otp")

    role = request.user.userprofile.role

    if role == "owner":
        return render(request, "accounts/owner_dashboard.html", {
            "my_ads": request.user.userprofile.ads.all(),
            "requests": request.user.userprofile.owner_requests.all()
        })

    elif role == "pharmacist":
        return render(request, "accounts/pharmacist_dashboard.html", {
            "ads": Ad.objects.all(),
            "my_requests": request.user.userprofile.pharmacist_requests.all()
        })

    elif role == "admin":
        return render(request, "accounts/admin_dashboard.html", {
            "users": UserProfile.objects.all(),
            "ads": Ad.objects.all(),
            "stats": {
                "users": UserProfile.objects.count(),
                "ads": Ad.objects.count(),
                "requests": Request.objects.count()
            }
        })
