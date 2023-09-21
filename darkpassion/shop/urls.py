from django.urls import path
from . import views
app_name = "shop"
urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    # path('images', views.display_all_images, name='get_products'),
    # path('display-images/', views.display_all_images, name='display_all_images')
]