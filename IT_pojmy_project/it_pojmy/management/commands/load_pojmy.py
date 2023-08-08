from django.core.management.base import BaseCommand
from it_pojmy.models import ItPojem
import json


class Command(BaseCommand):
    def handle(self, **options):
        with open('it_pojmy/data/tech-names.json', encoding='utf-8') as soubor:
            data = json.load(soubor)
            for item in data:
                ItPojem.objects.update_or_create(
                    zkratka=item['id'],
                    defaults={'nazev': item['name']}
                )
                print(item)