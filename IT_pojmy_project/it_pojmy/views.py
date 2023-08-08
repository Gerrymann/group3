
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, ListView
from it_pojmy.models import ItPojem, Clanek, Komentar
from it_pojmy.forms import ClanekForm

# Create your views here.
def index(request):
    return render(request, 'it_pojmy/index.html')

def seznam(request):
    all_pojmy = ItPojem.objects.all()
    return render(request, 'it_pojmy/seznam.html', context={'all_pojmy': all_pojmy})

def detail(request, zkratka):
    return HttpResponse('TOTO JE DETAIL' + zkratka)

def seznam_clanku(request):
    clanky = Clanek.objects.order_by('-id')[:100]
    return render(request, 'it_pojmy/clanek_list.html', context={'clanky': clanky})


from django.views.generic import ListView

class ClanekList(ListView):
    model = Clanek
    context_object_name = 'clanky'
    paginate_by = 24


def detail_clanku(request, slug_url):

    clanek = Clanek.objects.get(slug=slug_url)

    return render(request, 'it_pojmy/clanek_detail.html', context={'clanek': clanek})

def novy_komentar(request):
    clanek_id = request.POST['clanek_id']
    autor = request.GET['autor']
    obsah = request.POST['obsah']

    Komentar.objects.create(
        autor=autor,
        obsah=obsah,
        clanek_id=clanek_id,
    )
    clanek = Clanek.objects.get(id=clanek_id)

    return redirect(
        reverse('it_pojmy:detail_clanku', kwargs={'slug_url': clanek.slug})
    )


class ClanekCreateView(CreateView):
    form_class = ClanekForm
    success_url = ''
    template_name = ''



