from django.db import models
from django.shortcuts import reverse

# Create your models here.



class ItPojem(models.Model):
    zkratka = models.SlugField(max_length=100)
    nazev = models.CharField(max_length=100)
    popis = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.nazev

class Kategorie(models.Model):
    slug = models.SlugField(max_length=100) # blank null
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev


class Clanek(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    nazev = models.CharField(max_length=100)
    popis = models.CharField(blank=True, max_length=500)
    datum = models.DateTimeField(blank=True, null=True, auto_now=True)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.nazev

    def get_absolute_url(self):
        return reverse('it_pojmy:detail_clanku', kwargs={'slug_url': self.slug})

class Komentar(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    nazev = models.CharField(max_length=100)
    popis = models.CharField(blank=True, max_length=500)
    datum = models.DateTimeField(blank=True, null=True)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.PROTECT, null=True, blank=True)