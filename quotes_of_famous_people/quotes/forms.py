from django import forms
from .models import QuoteDjango, AuthorDjango


class AddQuote(forms.ModelForm):
    quote = forms.CharField(min_length=3, max_length=10000, required=True, widget=forms.TextInput())
    tags = forms.CharField(min_length=3, max_length=10000, required=True, widget=forms.TextInput())
    author = forms.ModelChoiceField(queryset=AuthorDjango.objects.all(), empty_label="Select author", required=True)

    class Meta:
        model = QuoteDjango
        fields = ['quote', 'tags', 'author']


class AddAuthor(forms.ModelForm):
    fullname = forms.CharField(min_length=3, max_length=50, required=True, widget=forms.TextInput())
    born_date = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput())
    born_location = forms.CharField(min_length=3, max_length=50,widget=forms.TextInput())
    description = forms.CharField(min_length=3, widget=forms.TextInput())


    class Meta:
        model = AuthorDjango
        fields = ['fullname', 'born_date', 'born_location', 'description']
