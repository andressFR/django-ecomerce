from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.

def get_file_path(request,filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s0 % (nowTime.original_filename)"
    return os.path.join('uploads/',filename)

#tabla categoria
class Category(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True)

    #metodo que retorna el nombre de categoria
    def __str__(self):
        return self.name

#tabla de productos
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#llave foranea
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    small_description = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2)
    selling_price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True)

    digital = models.BooleanField(default=False, null=True, blank=False)

    #metodo que retorna el nombre de categoria
    def __str__(self):
        return self.name
    
    #metodo que retorna la direccion de las imagenes
    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        
        return url

#Tabla del carrito de compras
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)


#-------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------#


#modelo cliente 
"""class Customer(models.Model):
    #campos de la tabla
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)#usuario
    name = models.CharField(max_length=200, null=True)#nombre
    email = models.CharField(max_length=200, null=True)#correo

    #metodo que devuelve el mombre
    def __str__(self):
        return self.name"""

    
#modelo orden   
class Order(models.Model):
     #campos de la tabla
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)#cliente (llave foranea)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)#orden completada
    transaction_id = models.CharField(max_length=200, null=True)#id de la transaccion
    
    #metodo que deuelve el id de la roden
    def __str__(self):
        return str(self.id)
    
    #metodo para verificar el envio
    @property
    def shopping(self):
        shopping = False
        orderitems = self.orderitem_set.all()

        """Ciclo que recorrera lo productos agregados al carrito, este verifica si el producto no es digital, nos servira para
        mostrar el formulario de direccion"""
        for i in orderitems:
            if i.product.digital == False:
                shopping = True

        return shopping
    
    #metodo que calcula el precio total de todos los productos
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    #metodo que calcula el total de procductos
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
#modelo orden articulo
class OrderItem(models.Model):
    #campos de la tabla
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True, null=True)#producto
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    #metodo que calcula el precio total de los prouctos mulltiplicando el precio * la cantidad
    @property
    def get_total(self):
        total = self.product.selling_price * self.quantity
        return total

 #modelo direccion de compra
class ShoppingAdress(models.Model):
    #campos de la tabla
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)#cliente
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)#orden
    address = models.CharField(max_length=200, null=False)#direccion
    city = models.CharField(max_length=200, null=False)#ciudad
    state = models.CharField(max_length=200, null=False)#estado
    zipcode = models.CharField(max_length=200, null=False)#codigo postal
    date_added = models.DateTimeField(auto_now_add=True)#fecha agregada

    #metodo que devuelve la direccion
    def __str__(self):
        return self.addres
    
