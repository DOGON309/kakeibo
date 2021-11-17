from django.shortcuts import render
from .models import seikyumodel

def indexview(request):
    params = {
        'title': '家計簿',
        'items': seikyumodel.objects.all(),
    }
    return render(request, 'kakeibo/index.html', params)

def detailview(request, id):
    params = {
        'title': '詳細',
        'items': seikyumodel.objects.get(id=id),
    }
    return render(request, 'kakeibo/detail.html', params)