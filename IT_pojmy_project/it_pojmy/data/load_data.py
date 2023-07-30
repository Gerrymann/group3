

import json
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_project_settings")
django.setup()



from it_pojmy.models import ItPojem

with open('tech-names.json', encoding='utf-8') as soubor:
    data = json.load(soubor)
    for item in data:
        print(item)
