from django.shortcuts import render, get_object_or_404
from .models import Product


def show_main(request):
    featured_products = Product.objects.filter(is_featured=True).order_by('total_sales')
    all_products = Product.objects.all().order_by('total_sales')
    context = {
        "name" : "Heraldo Arman",
        "class": "PBP - E",
        "featured_products": featured_products,
        "all_products": all_products,
    }  
    
    return render(request, "main/main.html", context=context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    context = {
        "product": product,
        "related_products": related_products,
    }
    return render(request, "main/product.html", context)