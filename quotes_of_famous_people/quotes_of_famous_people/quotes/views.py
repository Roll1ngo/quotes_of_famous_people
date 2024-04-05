import re
from collections import Counter

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import AuthorDjango, QuoteDjango
from .forms import AddQuote, AddAuthor


# Create your views here.
def main(request, page=1):
    quotes = QuoteDjango.objects.order_by('quote').all()
    quantity_page = 8
    paginator = Paginator(quotes, quantity_page)
    quotes_on_page = paginator.page(page)

    all_tags = QuoteDjango.objects.values_list('tags', flat=True)
    tag_counter = Counter()
    for tags in all_tags:
        for tag in tags:
            tag_counter[tag] += 1

    top_tags = [tag[0] for tag in tag_counter.most_common(10)]

    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page, 'top_tags': top_tags})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = AddQuote(request.POST)
        if form.is_valid():
            quote_data = form.cleaned_data
            tags_list = re.findall(r'\w+', quote_data['tags'])
            quote_data['tags'] = tags_list
            quote = QuoteDjango(**quote_data)
            quote.user = request.user
            quote.save()
            return redirect('quotes:root')
    else:
        form = AddQuote()
    return render(request, 'quotes/add_quote.html', {'form': AddQuote()})


@login_required
def add_author(request):
    if request.method == 'POST':
        form_author = AddAuthor(request.POST)
        if form_author.is_valid():
            add_user = form_author.save(commit=False)
            add_user.user = request.user
            add_user.save()
            return redirect('quotes:root')
    else:
        form_author = AddAuthor()
    return render(request, 'quotes/add_author.html', {'form_author': form_author})


def show_author(request, name):
    author = AuthorDjango.objects.get(fullname=name)
    return render(request, 'quotes/show_author.html', {'author': author})


def find_quotes_by_tag(request, name):
    founded_quotes = QuoteDjango.objects.filter(tags__contains=[name])
    return render(request, 'quotes/founded_quotes.html',
                  {'founded_quotes': founded_quotes, 'tag': name.capitalize()})
