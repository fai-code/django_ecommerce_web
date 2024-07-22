from .views import home, contact, about, login, navigation, base , new_product, new_orders, new_customers, new_suppliers, category
from django.urls import path

urlpatterns = [
    path('index/', home,name='index'),
    path('contact/',contact, name='contact'),
    path('about/',about, name='about'),
    path('login/', login, name='login'),
    path('navigation/', navigation, name = 'navigation'),
    path('base/', base, name = 'base'),
    path('new_product/', new_product, name='new_product'),
    path('new_orders/', new_orders, name='new_orders'),
    path('new_customers/', new_customers, name='new_customers'),
    path('new_suppliers/', new_suppliers, name='new_suppliers'),
    path('category/', category, name='category'),
]