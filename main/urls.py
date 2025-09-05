from django.urls import path
from main.views import show_main, product_detail

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
     path('<uuid:pk>/', product_detail, name='product_detail'),
]
