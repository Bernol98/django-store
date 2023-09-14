from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Product
class ProductListView(generic.ListView):
    template_name = "shop/all_products.html"
    context_object_name =  "all_products"
    def get_queryset(self):
        return Product.objects.all()

# Create your views here.
def all_products(request):
    products = Product.objects.filter(image__isnull=False)
    return render(request, 'all_products.html', {'products': products})
def get_product_image(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.image:
        with open(product.image.path, 'rb') as image_file:
            return HttpResponse(image_file.read(), content_type='image/jpeg')

#def detail(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, "polls/detail.html", {"question":question})