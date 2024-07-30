from django.shortcuts import render
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
# To authenticate user
def login (request):
    return render(request, 'login.html')

def navigation (request):
    return render (request, 'navigation.html')

def base (request):
    return render (request, 'base.html')

def orders (request):
    return render (request, 'orders.html')

def products (request):
    return render (request, 'products.html')

def suppliers (request):
    return render (request, 'suppliers.html')

def category(request):
    if request.method== 'POST':
        category_name = request.POST['category_name']
        description = request.POST['description']
        try:
            category.objects.create(
                category_name = category_name,
                description = description
        )
            return render (request, 'category.html')
    
        except IntegrityError: 
            error ="Duplicate product information"
        except  Exception as e:
            error = str(e) 
        
        context={"error":error}
        return render(request, 'category.html',context)
    
def new_products(request):
    if request.method=='POST':
        product_type = request.POST['product_type']
        product_name = request.POST['product_name']
        quantity_per_unit = request.POST['quantity_per_unit']
        unit_price = request.POST['unit_price']
        unit_in_stock = request.POST['unit_in_stock']
        unit_order = request.POST['unit_order']
        re_order_level = request.POST['re_order_level']
       
        try:
            Products.objects.create(
                product_type = product_type,
                product_name = product_name,
                quantity_per_unit= quantity_per_unit,
                unit_price = unit_price,
                unit_in_stock = unit_in_stock,
                unit_order = unit_order,
                re_order_level = re_order_level

        )
           

        except IntegrityError: 
            error ="Duplicate product information"
        except  Exception as e:
            error = str(e) 
            
        context = {"error":error}
        return render(request, 'new_products.html', context)
    
    return render (request, 'new_products.html')

def new_orders (request):
    if request.method=='POST':
        customers = request.POST[f"{Customers.first_name}"]
        products = request.POST[f"{Products.product_name}"]
        category = request.POST[f"{Category.category_name}"]
        order_type = request.POST['order_type']
        order_quantity =request.POST['order_quantity']
        name = request.POST['name']
        order_price = request.POST['order_price']
        order_discount = request.POST['order_discount']

        try:
            Orders.objects.create(
                order_type = order_type,
                order_quantity = order_quantity,
                oder_name = order_quantity,
                order_price=order_price,
                order_discount = order_discount
        )
           
        
        except IntegrityError: 
            error ="Duplicate product information"
        except  Exception as e:
            error = str(e) 
        
        context = {"error":error}
        return render (request,'new_orders.html',context)
   
    return render (request,'new_orders.html')
    
def new_customers (request):
    if request.method== 'POST':
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']

        try:
            Customers.objects.create( 
                first_name = first_name,
                last_name = last_name,
                phone_number = phone_number 
                )
        
           
        except IntegrityError: 
                error ="Duplicate product information"
        except  Exception as e:
            error = str(e) 
        context={"error": error}  
        return render (request, 'new_customers.html', context)

    return render (request, 'new_customers.html')

def new_suppliers (request):
    if request.method== 'POST':
         name = request.POST['name']
         address =request.POST['address']
         postal_code = request.POST['postal_code']
         contact_number = request.POST['contact_number']
         contact_title = request.POST['contact_title']
         items = request.POST['items']
         home_page = request.POST['home_page']
         company_name = request.POST['company_name']
         country = request.POST['country']
         county = request.POST['county']
          
         try:
            Suppliers.objects.create(
                name = name,
                address = address,
                postal_code = postal_code,
                contact_number =  contact_number,
                contact_title = contact_title,
                items = items,
                home_page = home_page,
                company_name = company_name,
                country = country,
                county =county
            )
         
    
         except IntegrityError: 
            error ="Duplicate product information"
         except  Exception as e:
          error = str(e) 
    
         context={"error": error}
         return render (request,'new_suppliers.html', context)

    return render (request, 'new_suppliers.html')
    

