from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product


class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Productos'
        print(context)
        return context


class ProductDetailView(DetailView): #Search by id -> pk. This class takes the id from url route
    template_name = 'products/product.html'
    model = Product
