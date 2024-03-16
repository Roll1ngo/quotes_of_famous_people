import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import AuthorDjango, QuoteDjango
from django.core.paginator import Paginator
from .forms import AddQuote, AddAuthor


# Create your views here.
def main(request, page=1):
    quotes = QuoteDjango.objects.order_by('quote').all()
    quantity_page = 8
    paginator = Paginator(quotes, quantity_page)
    quotes_on_page = paginator.page(page)

    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = AddQuote(request.POST)
        if form.is_valid():
            quote_data = form.cleaned_data
            tags_list = re.findall(r'\w+', quote_data['tags'])
            quote_data['tags'] = tags_list
            quote = QuoteDjango(**quote_data)
            quote.save()
            return redirect('quotes:root')
    else:
        form = AddQuote()
    return render(request, 'quotes/add_quote.html', {'form': form})


@login_required
def add_author(request):
    if request.method == 'POST':
        form_author = AddAuthor(request.POST)
        if form_author.is_valid():
            new_author = form_author.save()
            return redirect('quotes:root')
    else:
        form_author = AddAuthor()
    return render(request, 'quotes/add_author.html', {'form_author': form_author})


def show_author(request, name):
    author = AuthorDjango.objects.get(fullname=name)
    return render(request, 'quotes/show_author.html', {'author': author})
