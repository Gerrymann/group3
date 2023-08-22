from django.shortcuts import render
from eshop.models import Kategorie, Produkt, Znacka


def index(request):
    kategorie = Kategorie.objects.all()
    return render(request, 'eshop/index.html', context={'kategorie': kategorie})


def kategorie_list(request):
    object_list = Kategorie.objects.all()
    return render(request, 'eshop/kategorie.html', context={'object_list': object_list})


def kategorie_detail(request, slug):
    kategorie = Kategorie.objects.get(slug=slug)
    return render(request, 'eshop/kategorie_detail.html', context={'kategorie': kategorie})


def znacka_detail(request, slug):
    znacka = Znacka.objects.get(slug=slug)
    produkty = Produkt.objects.filter(znacka=znacka)
    return render(request, 'eshop/znacka.html', context={'znacka': znacka, 'produkty': produkty})


def produkt_detail(request, slug, pk):
    produkt = Produkt.objects.get(slug=slug, pk=pk)
    return render(request, 'eshop/produkt.html', context={'produkt': produkt})


def produkt_list(request):
    object_list = Produkt.objects.all()
    return render(request, 'eshop/produkt_list.html', context={'object_list': object_list})
