from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from django.http import HttpResponse

from pharmacy_ads.app_ads.models import Ad


def ads_list(request):
    return HttpResponse("لیست آگهی‌ها")


def ads_detail(request, id):
    ad = get_object_or_404(Ad, id=id)
    return render(request, "ads/ads_detail.html", {"ad": ad})

