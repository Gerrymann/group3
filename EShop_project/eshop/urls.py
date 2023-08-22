from django.urls import path
from eshop import views

app_name = 'eshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('kategorie/', views.kategorie_list, name='kategorie'),
    path('produkty/', views.produkt_list, name='produkt_list'),
    path('<slug:slug>/', views.kategorie_detail, name='kategorie_detail'),
    path('znacka/<slug:slug>/', views.znacka_detail, name='znacka_detail'),
    path('p/<slug:slug>/<int:pk>/', views.produkt_detail, name='produkt_detail'),
]
