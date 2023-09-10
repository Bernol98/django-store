from django.shortcuts import render
from django.views import generic
from .models import Product
class ProductListView(generic.ListView):
    template_name = "shop/index.html"
    context_object_name =  "all_products"
    def get_queryset(self):
        return Product.objects.all()

# Create your views here.

def main_page_product_list(requset):
    images = Product.objects.all()
    return render(requset, "shop/index.html",{"images":images})
