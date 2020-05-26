from django.urls import path
from . import views

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'), #Search must be the first url to avoid error with slug
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product') #id -> primary key
]