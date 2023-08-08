from django.core.management.base import BaseCommand
from it_pojmy.models import Clanek


class Command(BaseCommand):
    def handle(self, **options):
        for i in range(10000):
            Clanek.objects.update_or_create(
                slug=f'test-clanek-{i}',
                defaults={'nazev': f'Test článek {i}'},
            )
            print(i)