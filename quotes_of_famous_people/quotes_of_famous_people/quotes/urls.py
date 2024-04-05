
from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("add_quote/", views.add_quote, name="add_quote"),
    path("add_author/", views.add_author, name="add_author"),
    path("author/<path:name>/", views.show_author, name="show_author"),
    path("quote_list/<path:name>/", views.find_quotes_by_tag, name="find_quotes_by_tag")
]
