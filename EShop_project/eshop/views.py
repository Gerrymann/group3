from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView
from django.shortcuts import render
from eshop.models import Kategorie


def kategorie(request):
    all_kategorie = Kategorie.objects.all()
    return render(request, 'eshop/kategorie.html', context={'all_kategorie': all_kategorie})