from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from products.models import Product, Manufacturer


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    
    
class ProductListView(ListView):
    model = Product
    tmeplate_name = "products/product_list.html"
    