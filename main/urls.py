from django.urls import path
from main.views import show_main, product_detail, add_employee, view_xml, view_json, view_xml_by_id, view_json_by_id, add_product, add_brand, login_views, register_views, logout_user, profile_views, delete_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('<uuid:pk>/', product_detail, name='product_detail'),
    path('employees/', add_employee, name='add_employee'),
    path('xml/', view_xml, name='view_xml'),
    path('json/', view_json, name='view_json'),
    path('xml/<uuid:pk>/', view_xml_by_id, name='view_xml_by_id'),
    path('json/<uuid:pk>/', view_json_by_id, name='view_json_by_id'),
    path('add_product/', add_product, name='add_product'),
    path('add_brand/', add_brand, name='add_brand'),
    path('login/', login_views, name='login'),
    path('register/', register_views, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile_views, name='profile'),
    path('delete_product/<uuid:pk>/', delete_product, name='delete_product')
]
