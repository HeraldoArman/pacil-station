from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.utils.html import strip_tags
from .models import Product, Employee
from .forms import ProductForm, BrandForm, LoginForm, RegisterForm, CarForm
import datetime
import json
import requests


def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        product = Product(
            user=request.user,
            name=strip_tags(data.get('name')),
            price=data.get('price'),
            description=strip_tags(data.get('description')),
            thumbnail=strip_tags(data.get('thumbnail')),
            flip_thumbnail=data.get('flip_thumbnail', False),
            category=strip_tags(data.get('category')),
            is_featured=data.get('is_featured', False),
            size=strip_tags(data.get('size')),
            rating=data.get('rating', 0.0),
            stock=data.get('stock', 0),
            total_sales=data.get('total_sales', 0),
            brand_id=data.get('brand_id') if data.get('brand_id') else None
        )
        product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)




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

    context = {
        "product": product,
    }
    return render(request, "main/product.html", context)

@login_required(login_url='/login/')
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)
    product.delete()
    return redirect('main:profile')

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
    
    
    
@login_required(login_url='/login/')
def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:profile')
    context = {
        "form": form,
    }
    return render(request, "main/add_product.html", context)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)
    try:
        data = json.loads(request.body)
        product = Product.objects.create(
            user=request.user,
            name=data.get('name'),
            price=data.get('price'),
            description=data.get('description'),
            thumbnail=data.get('thumbnail'),
            flip_thumbnail=data.get('flip_thumbnail', False),
            category=data.get('category'),
            is_featured=data.get('is_featured', False),
            size=data.get('size'),
            rating=data.get('rating', 0.0),
            stock=data.get('stock', 0),
            total_sales=data.get('total_sales', 0),
            brand_id=data.get('brand_id') if data.get('brand_id') else None
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Product created successfully',
            'product': {
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'thumbnail': product.thumbnail,
                'category': product.category,
                'rating': product.rating,
                'stock': product.stock,
                'total_sales': product.total_sales,
                'brand': product.brand.name if product.brand else None
            }
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': 'Failed to add product', 'detail': str(e)}, status=400)


def get_product_form_ajax(request):
    from .models import Product
    from .forms import ProductForm
    
    form = ProductForm()
    brands = Product.Brand.objects.all()
    
    return JsonResponse({
        'brands': [{'id': str(brand.id), 'name': brand.name} for brand in brands]
    }) 

@csrf_exempt
def get_products_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)
    products = Product.objects.filter(user=request.user)
    data = []
    for product in products:
        data.append({
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'flip_thumbnail': product.flip_thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'size': product.size,
            'rating': product.rating,
            'stock': product.stock,
            'total_sales': product.total_sales,
            'brand': product.brand.name if product.brand else None,
            # 'user': product.user.username,
            'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return JsonResponse({'products': data})

@csrf_exempt
def edit_product_ajax(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)
    try:
        product = get_object_or_404(Product, pk=pk, user=request.user)
        if request.method == "PUT":
            data = json.loads(request.body)  # Changed from json.load() to json.loads()
            
            product.name = data.get('name', product.name)
            product.price = data.get('price', product.price)
            product.description = data.get('description', product.description)
            product.thumbnail = data.get('thumbnail', product.thumbnail)
            product.flip_thumbnail = data.get('flip_thumbnail', product.flip_thumbnail)
            product.category = data.get('category', product.category)
            product.is_featured = data.get('is_featured', product.is_featured)
            product.size = data.get('size', product.size)
            product.rating = data.get('rating', product.rating)
            product.stock = data.get('stock', product.stock)
            product.total_sales = data.get('total_sales', product.total_sales)
            
            if data.get('brand_id'):
                product.brand_id = data.get('brand_id')
            
            product.save()
            return JsonResponse({
                'success': True,
                'message': 'Product updated successfully',
                'product': {
                    'id': str(product.id),
                    'name': product.name,
                    'price': product.price,
                    'description': product.description,
                    'thumbnail': product.thumbnail,
                    'category': product.category,
                    'rating': product.rating,
                    'stock': product.stock,
                    'brand': product.brand.name if product.brand else None
                }
            })
            
        elif request.method == 'GET':
            return JsonResponse({
                'product': {
                    'id': str(product.id),
                    'name': product.name,
                    'price': product.price,
                    'description': product.description,
                    'thumbnail': product.thumbnail,
                    'flip_thumbnail': product.flip_thumbnail,
                    'category': product.category,
                    'is_featured': product.is_featured,
                    'size': product.size,
                    'rating': product.rating,
                    'stock': product.stock,
                    'total_sales': product.total_sales,
                    'brand_id': product.brand.id if product.brand else None,
                    'brand': product.brand.name if product.brand else None
                }
            })
            
    except Exception as e:
        return JsonResponse({'success': False, 'message': 'Failed to edit product', 'detail': str(e)}, status=400)

@csrf_exempt
@require_POST
def delete_product_ajax(request, pk):
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)
    try:
        product = get_object_or_404(Product, pk=pk, user=request.user)
        product.delete()
        return JsonResponse({'success': True, 'message': 'Product deleted successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': 'Failed to delete product', 'detail': str(e)}, status=400)

            
            
            
@login_required(login_url='/login/')
def edit_product(request, pk):
    product_data = get_object_or_404(Product, pk=pk, user=request.user)
    form = ProductForm(request.POST or None, instance=product_data)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:profile')
    context = {
        "form": form,
    }    
    return render(request, "main/edit_product.html", context)

@login_required(login_url='/login/')
def add_brand(request):
    form = BrandForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:add_product')
    context = {
        "form": form,
    }
    return render(request, "main/add_brand.html", context)


def login_views(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'main/login.html', context)

def register_views(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'main/register.html', context)


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.delete_cookie('last_login')
    return redirect('main:show_main')


@login_required(login_url='/login/')
def profile_views(request):
    last_login_raw = request.COOKIES.get('last_login', 'Never')
    if last_login_raw != 'Never':
        try:
            last_login_dt = datetime.datetime.fromisoformat(last_login_raw)
            last_login = last_login_dt.strftime('%A, %d %B %Y %H:%M:%S')
        except Exception:
            last_login = last_login_raw
    else:
        last_login = 'Never'
        
        
    my_product = Product.objects.filter(user=request.user)
    context = {
        'last_login': last_login,
        'products' : my_product,
    }
    return render(request, 'main/profile.html', context)

def add_car(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:show_main')
    context = {
        "form": form,
    }
    return render(request, "main/add_car.html", context)


def ajax_products(request):
    return render(request, 'main/ajax_products.html')



@csrf_exempt
def ajax_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            if not username or not password:
                return JsonResponse({
                    'success': False,
                    'message': 'Username and password are required'
                }, status=400)
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                response_data = {
                    'success': True,
                    'message': 'Login successful',
                    'redirect_url': reverse('main:show_main')
                }
                response = JsonResponse(response_data)
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid username or password'
                }, status=400)
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'An error occurred during login',
                'detail': str(e)
            }, status=500)
    
    return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

@csrf_exempt
def ajax_register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Create form with data
            form = RegisterForm(data)
            
            if form.is_valid():
                user = form.save()
                return JsonResponse({
                    'success': True,
                    'message': 'Registration successful',
                    'user_id': user.id,
                    'username': user.username
                })
            else:
                # Return form errors
                errors = {}
                for field, error_list in form.errors.items():
                    errors[field] = [str(error) for error in error_list]
                
                return JsonResponse({
                    'success': False,
                    'message': 'Registration failed',
                    'errors': errors
                }, status=400)
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'An error occurred during registration'
            }, status=500)
    
    return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

def ajax_auth(request):
    return render(request, 'main/ajax_auth.html')