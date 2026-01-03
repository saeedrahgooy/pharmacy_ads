from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_otp, name='login_otp'),
    path('verify/', views.verify_otp, name='verify_otp'),
    path('choose-role/', views.choose_role, name='choose_role'),
    path('logout/', views.logout_view, name='logout'),
]