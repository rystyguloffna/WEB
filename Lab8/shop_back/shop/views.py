from django.shortcuts import render

from .models import Category,Product
from django.http import JsonResponse,HttpResponse

# Create your views here
def show_products(requests):
    products = list(Product.objects.values())
    return JsonResponse(products,safe=False)

def show_product(requests,product_id):
    try:
        product = list(Product.objects.filter(id=product_id).values())
        return JsonResponse(product,safe=False)
    except:
        return HttpResponse("NOT FOUND")


def show_categories(request):
    categories = list(Category.objects.values())
    return JsonResponse(categories,safe=False)

def show_category(request,category_id):
    try:
        category = list(Category.objects.filter(id=category_id).values())
        return JsonResponse(category,safe=False)
    except:
        return HttpResponse("NOT FOUND")