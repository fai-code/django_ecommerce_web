from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
   
    def __str__(self) -> str:
        return self.first_name + self.last_name

class Suppliers(models.Model):
    products = models.ForeignKey("Products", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    contact_number = models.CharField(max_length=20)
    contact_title = models.CharField(max_length=20)
    items = models.CharField(max_length=10)
    home_page = models.CharField(max_length=10)
    company_name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    county = models.CharField(max_length=10)
    

    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    product_type = models.CharField(max_length=8)
    product_name = models.CharField(max_length=8)
    quantity_per_unit = models.IntegerField()
    unit_price = models.DecimalField(max_digits=8,decimal_places=2)
    unit_in_stock = models.IntegerField()
    unit_order = models.IntegerField()
    re_order_level = models.IntegerField()
 
    def __str__(self) -> str:
        return self.product_name

class Orders(models.Model):
    Customers = models.ForeignKey("Customers", on_delete=models.CASCADE)
    Products = models.ForeignKey("products", on_delete=models.CASCADE)
    Category = models.ForeignKey("category", on_delete=models.CASCADE)
    order_type = models.CharField(max_length=10)
    order_quantity = models.IntegerField()
    name = models.CharField(max_length=7)
    order_price = models.DecimalField(max_digits=8,decimal_places=2)
    order_discount = models.IntegerField()
     
    def __str__(self) -> str:
        return self.order_name

class category(models.Model):
    category_name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
     
    def __str__(self) -> str:
        return self.category_name
