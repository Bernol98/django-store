from django.shortcuts import render
from django.views import generic
from .models import Product
class ProductListView(generic.ListView):
    template_name = "shop/product_list.html"
    context_object_name =  "all_products"
    def get_queryset(self):
        return Product.objects.all()

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    return render(request, "polls/index.html", all_products)