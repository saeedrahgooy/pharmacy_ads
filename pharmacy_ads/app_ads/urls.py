# app_ads/urls.py
from django.urls import path
from . import views

app_name = "ads"

urlpatterns = [
    path("", views.ads_list, name="list"),
    path("<int:id>/", views.ads_detail, name="detail"),
]
