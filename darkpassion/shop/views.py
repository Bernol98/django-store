from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Product
from django.views import generic
from .models import Product

class ProductListView(generic.ListView):
    template_name = "shop/all_products.html"
    context_object_name = "all_products"

    def get_queryset(self):
        # Return a queryset of products with images
        return Product.objects.exclude(image__isnull=True)


# Create your views here.
# def all_products(request):
#     products = Product.objects.all()
#     return render(request, 'all_products.html', {'products': products})

# def display_all_images(request):
#     products_with_images = Product.objects.exclude(image__isnull=True)
#     return render(request, 'display_images.html', {'products_with_images': products_with_images})

#def detail(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, "polls/detail.html", {"question":question})