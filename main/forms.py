from django.forms import ModelForm
from .models import Product
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Car

class ProductForm(ModelForm):
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
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Username",
                "autocomplete": "username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Password",
                "autocomplete": "current-password",
            }
        )
    )
    
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Username",
                "autocomplete": "username",
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Password",
                "autocomplete": "new-password",
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Confirm Password",
                "autocomplete": "new-password",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "brand", "stock"]
