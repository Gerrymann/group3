from django.urls import path
from it_pojmy import views




urlpatterns = [
    path('', views.index),
    path('seznam/', views.seznam),
    path('detail/<slug:zkratka>/', views.detail),
]