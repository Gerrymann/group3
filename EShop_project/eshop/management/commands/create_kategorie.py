from django.core.management.base import BaseCommand
from eshop.models import Kategorie


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Command is called")
        path = 'eshop/management/data/kategorie.txt'
        with open(path, encoding='UTF-8') as soubor:
            nad_kategorie = None
            for radek in soubor:
                radek = radek.strip()
                if radek.endswith(':'):
                    print("vytvořena nadkategorie", radek)
                    nad_kategorie, is_created = Kategorie.objects.update_or_create(nazev=radek[:-1])
                else:
                    print("vytvořena kategorie", radek, nad_kategorie)
                    Kategorie.objects.update_or_create(nazev=radek, nadkategorie=nad_kategorie)


