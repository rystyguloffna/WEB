from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products',views.show_products),
    path('product/<int:product_id>',views.show_product),
    path('categories',views.show_categories),
    path('category/<int:category_id>',views.show_category),
]