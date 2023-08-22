from eshop.models import Kategorie, Znacka


def kategorie_context(request):
    kategorie = Kategorie.objects.select_related('nadkategorie')
    znacky = Znacka.objects.all()

    return {
        'KATEGORIE': kategorie,
        'ZNACKY': znacky,
    }
