from django.shortcuts import render
from .models import AuthorDjango, QuoteDjango
from django.core.paginator import Paginator



# Create your views here.
def main(request, page=1):
    quotes = QuoteDjango.objects.all()
    quantity_page = 8
    paginator = Paginator(quotes, quantity_page)
    quotes_on_page = paginator.page(page)

    return render(request, template_name='quotes/index.html', context={'quotes': quotes_on_page})
