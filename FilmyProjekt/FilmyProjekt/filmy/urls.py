from django.urls import path
from filmy import views


app_name = 'filmy'

urlpatterns = [
    path('seznam/', views.seznam, name='seznam'),
    path('seznam/json/', views.seznam_json, name='seznam_json'),
    path('detail/<slug:slug>/', views.detail, name='detail'),

    path('seznam/hercu/', views.seznam_hercu, name='seznam_hercu'),
    path('detail-herce/<slug:slug>/', views.detail_herce, name='detail_herce'),
]


