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
        return context


class ProductDetailView(DetailView): #Search by id -> pk. This class takes the id from url route
    #This view returns an object called 'product' that we can use in product.html template
    template_name = 'products/product.html'
    model = Product


class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.query())

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['counter'] = context['product_list'].count()
        return context

