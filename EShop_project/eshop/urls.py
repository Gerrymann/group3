from django.urls import path
from eshop import views


app_name = 'eshop'

urlpatterns = [
    path('kategorie/', views.kategorie, name='kategorie')
]