from django import forms
from .models import QuoteDjango, AuthorDjango


class AddQuote(forms.ModelForm):
    quote = forms.CharField(
        min_length=3, max_length=10000, required=True,
        widget=forms.TextInput(attrs={'id': 'quote'})
    )
    tags = forms.CharField(
        min_length=3, max_length=10000, required=True,
        widget=forms.TextInput(attrs={'id': 'tags'})
    )
    author = forms.ModelChoiceField(
        queryset=AuthorDjango.objects.all(), empty_label="Select author", required=True,
        widget=forms.Select(attrs={'id': 'author'})
    )

    class Meta:
        model = QuoteDjango
        fields = ['quote', 'tags', 'author']


class AddAuthor(forms.ModelForm):
    fullname = forms.CharField(
        min_length=3, max_length=50, required=True,
        widget=forms.TextInput(attrs={'id': 'fullname'})
    )
    born_date = forms.CharField(
        min_length=3, max_length=50,
        widget=forms.TextInput(attrs={'id': 'born_date'})
    )
    born_location = forms.CharField(
        min_length=3, max_length=50,
        widget=forms.TextInput(attrs={'id': 'born_location'})
    )
    description = forms.CharField(
        min_length=3, widget=forms.TextInput(attrs={'id': 'description'}))

    class Meta:
        model = AuthorDjango
        fields = ['fullname', 'born_date', 'born_location', 'description']
