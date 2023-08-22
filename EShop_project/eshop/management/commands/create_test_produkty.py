import json, random
from django.core.management.base import BaseCommand
from eshop.models import Produkt, Znacka, Kategorie
from django.utils.text import slugify


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(r'eshop\management\data\test_data.json', encoding='utf-8') as soubor:
            data = json.load(soubor)

            for item in data['produkty']:
                znacka_slug = slugify(item['značka'])
                znacka = Znacka.objects.get(slug=znacka_slug)
                # znacka = Znacka.objects.first()

                kategorie_slug = slugify(item['kategorie'])
                kategorie = Kategorie.objects.get(slug=kategorie_slug)
                # print(znacka, znacka.id, kategorie, kategorie.id)

                produkt, created = Produkt.objects.update_or_create(
                    nazev=item['název'],
                    defaults=dict(
                        popis="Toto je popis pro " + item['název'],
                        aktualni_cena=random.randint(100, 9999),
                        znacka=znacka,
                        mnozstvi=random.randint(1, 100),
                    )
                )

                produkt.kategorie.add(kategorie)

                print(produkt, created)
