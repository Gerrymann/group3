from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class SlugNazevModel(models.Model):
    nazev = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nazev

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nazev)
        super().save(*args, **kwargs)


class Kategorie(SlugNazevModel):
    nadkategorie = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='podkategorie',
    )

    def get_absolute_url(self):
        return reverse('eshop:kategorie_detail', kwargs={'slug': self.slug})


class Znacka(SlugNazevModel):
    logo = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('eshop:znacka_detail', kwargs={'slug': self.slug})


class Produkt(SlugNazevModel):
    popis = models.TextField(max_length=1000, blank=True)
    aktualni_cena = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    znacka = models.ForeignKey(
        Znacka,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    kategorie = models.ManyToManyField(Kategorie, blank=True)
    mnozstvi = models.PositiveIntegerField(default=0)
    vlastnosti = models.JSONField(default=dict, blank=True)

    def get_absolute_url(self):
        return reverse('eshop:produkt_detail', kwargs={'slug': self.slug, 'pk': self.pk})


class Cena(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.PROTECT)
    hodnota = models.DecimalField(max_digits=10, decimal_places=2)
    plati_od = models.DateField()
    plati_do = models.DateField()
