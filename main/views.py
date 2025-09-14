from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Employee
from django.http import HttpResponse
from django.core import serializers
from .forms import ProductForm, BrandForm

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

def add_employee(request):
    
    employees = Employee.objects.create(name="Aldo", age=20, persona="suka tidur")
    
    context = {
        "employees" : employees
    }
    return render(request, "main/employee.html", context)


def view_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")


def view_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")


def view_xml_by_id(request, pk):
    try:
        productData = get_object_or_404(Product, pk=pk)
        xml_data = serializers.serialize("xml", [productData])
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)
        
    
def view_json_by_id(request, pk):
    try:
        productData = get_object_or_404(Product, pk=pk)
        json_data = serializers.serialize("json", [productData])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)
    
    
def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:show_main')
    context = {
        "form": form,
    }
    return render(request, "main/add_product.html", context)
    
    
def add_brand(request):
    form = BrandForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:add_product')
    context = {
        "form": form,
    }
    return render(request, "main/add_brand.html", context)