
from django.shortcuts import render, reverse, HttpResponse, Http404
from django.http import JsonResponse
from django.utils.text import slugify
from filmy.data import filmy_data

# Create your views here.
def seznam(request):
    slug = slugify(request.GET.get('text'))

    if slug:
        data = {}
        for key_film in filmy_data:
            if key_film.startswith(slug):
                data[key_film] = filmy_data[key_film]


        context = {'filmy_data': data}
    else:
        context = {'filmy_data': filmy_data}

    return render(request, 'filmy/seznam.html', context=context)

def detail(request, slug):
    if slug in filmy_data:
        film = filmy_data[slug]
        response = render(request, 'filmy/detail.html', context={'film': film})
        response['MOJE-DATA'] = 'HELLO'
        #response['Content-Type'] = 'application/json; charset=utf-8'
        return response
    else:
        raise Http404('Film nebyl nalezen')

def seznam_json(request):
    return JsonResponse(filmy_data)


"""
0) mít data v dict
1) views.py
seznam_hercu -> return render() + html
detail_herce -> return render() + html

2) urls.py
/seznam_herci/
-> /filmy/seznam-hercu/

/detail-herce/<slug:slug>/
-> /filmy/detail-herce/jim_carrey/


3) nedělat search
"""