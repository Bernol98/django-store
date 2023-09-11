from django.urls import path
from . import views
app_name = "shop"
urlpatterns = [
    path("", views.ProductListView.as_view(),name="shop"),
    path('index/', views.main_page_product_list, name='index'),
]