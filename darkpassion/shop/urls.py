from django.urls import path
from . import views
app_name = "shop"
urlpatterns = [
    path("", views.ProductListView.as_view(),name="shop"),
    path('images', views.all_products, name='get_products'),
]