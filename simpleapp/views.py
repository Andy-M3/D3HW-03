from datetime import datetime

from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import *


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду!"
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class NewsList(ListView):
    model = News1
    ordering = '-data'
    template_name = 'news.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = News1
    template_name = 'one_news.html'
    context_object_name = 'one_news'