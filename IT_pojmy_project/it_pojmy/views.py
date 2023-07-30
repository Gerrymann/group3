
from django.http import HttpResponse
from django.shortcuts import render
from it_pojmy.models import ItPojem

# Create your views here.
def index(request):
    return render(request, 'it_pojmy/index.html')

def seznam(request):
    all_pojmy = ItPojem.objects.all()
    return render(request, 'it_pojmy/seznam.html', context={'all_pojmy': all_pojmy})

def detail(request, zkratka):
    return HttpResponse('TOTO JE DETAIL' + zkratka)

def load_data(request):
    # takto prosim ne

    import json

    with open('it_pojmy/data/tech-names.json', encoding='utf-8') as soubor:
        data = json.load(soubor)
        for item in data:
            ItPojem.objects.update_or_create(
                zkratka=item['id'],
                defaults={'nazev': item['name']},
            )
            print(item)
    return HttpResponse('Data Loaded')
