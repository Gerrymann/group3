from django.db import models

# Create your models here.



class ItPojem(models.Model):
    zkratka = models.SlugField(max_length=100) # blank null
    nazev = models.CharField(max_length=100)
    popis = models.CharField(max_length=500, blank=True)