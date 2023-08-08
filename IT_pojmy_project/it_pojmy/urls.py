from django.urls import path
from it_pojmy import views




urlpatterns = [
    path('', views.index, name='index'),
    path('seznam/', views.seznam, name='seznam'),
    path('detail/<slug:zkratka>/', views.detail, name='detail'),
    path('novy-komentar/', views.novy_komentar, name='novy_komentar'),
    path('novy_clanek/', views.ClanekCreateView.as_view(), name='ClanekCreateView'),
    path('clanky/', views.seznam_clanku, name='seznam_clanku'),
    path('clanky2', views.ClanekList.as_view(), name='ClanekList'),
    path('clanky/<slug:slug_url>/', views.detail_clanku, name='detail_clanku')
]