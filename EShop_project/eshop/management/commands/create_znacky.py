from django.core.management.base import BaseCommand
from eshop.models import Znacka


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Command is called")
        path = 'eshop/management/data/znacky.txt'
        with open(path, encoding='UTF-8') as soubor:
            for radek in soubor:
                radek = radek.strip()
                print("creating", radek)
                Znacka.objects.update_or_create(nazev=radek)


