from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def login (request):
    return render(request, 'login.html')

def navigation (request):
    return render (request, 'navigation.html')

def base (request):
    return render (request, 'base.html')

def new_product (request):
    return render (request, 'new_product.html')

def new_orders (request):
    return render (request, 'new_orders.html')

def new_customers (request):
    return render (request, 'new_customers.html')

def new_suppliers (request):
    return render (request, 'new_suppliers.html')

def category (request):
    return render (request, 'category.html')