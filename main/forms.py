from django.forms import ModelForm
from .models import Product

from django import forms
from .models import Product, Car

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "flip_thumbnail", "category", "is_featured", "size", "rating", "stock", "total_sales", "brand"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "price": forms.NumberInput(attrs={"class": "input input-bordered w-full"}),
            "description": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered h-24 w-full",
                    "placeholder": "Product description",
                }
            ),
            "thumbnail": forms.URLInput(attrs={"class": "input input-bordered w-full"}),
            "flip_thumbnail": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "category": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "is_featured": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "size": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "rating": forms.NumberInput(attrs={"class": "input input-bordered w-full"}),
            "stock": forms.NumberInput(attrs={"class": "input input-bordered w-full"}),
            "total_sales": forms.NumberInput(attrs={"class": "input input-bordered w-full"}),
            "brand": forms.Select(attrs={"class": "select select-bordered w-full"}),
        }

class BrandForm(ModelForm):
    class Meta:
        model = Product.Brand
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        }
        
class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "brand", "stock"]