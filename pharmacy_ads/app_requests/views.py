from django.shortcuts import render

from django.http import HttpResponse

def requests_list(request):
    return HttpResponse("لیست درخواست‌ها")
