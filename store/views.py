from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse


import json
import datetime


# Create your views here.
#pagina principal
def home(request):
    if request.user.is_authenticated:
        # Obtiene o crea una orden para el usuario actual que aún no esté completa
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        # Obtiene todos los items de la orden
        items = order.orderitem_set.all()
        # Obtiene el total de items en el carrito
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request,'store/index.html',context)

#pagina de categorias
def collections(request):
    if request.user.is_authenticated:
        # Obtiene o crea una orden para el usuario actual que aún no esté completa
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        # Obtiene todos los items de la orden
        items = order.orderitem_set.all()
        # Obtiene el total de items en el carrito
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    category = Category.objects.filter(status=0)#objeto de la clase categoria
    products = Product.objects.all()
    context = {'category':category,'products':products, 'cartItems':cartItems}
    return render(request,'store/collections.html',context)

#pagina para categoria especifica
"""En esta funcion se filtra el slug de la categoria y se pasa como parametro en la url del 
navegador"""
def collectionsViews(request, slug):
    if request.user.is_authenticated:
        # Obtiene o crea una orden para el usuario actual que aún no esté completa
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        # Obtiene todos los items de la orden
        items = order.orderitem_set.all()
        # Obtiene el total de items en el carrito
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']


    if Category.objects.filter(slug=slug,status=0):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category':category, 'cartItems':cartItems, 'shopping':False}
        return render(request,'store/products/index.html',context)
    else:
        messages.warning(request,'No se encontro categoria')
        return redirect('collections')
    
#pagina de detalles de producto
def productview(request, cate_slug, prod_slug):
    if request.user.is_authenticated:
        # Obtiene o crea una orden para el usuario actual que aún no esté completa
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        # Obtiene todos los items de la orden
        items = order.orderitem_set.all()
        # Obtiene el total de items en el carrito
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']


    """si el slug del producto es igual al parametro cate_slug buscaremos el producto en la BD"""
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            #objeto que almacena el producto
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products':products, 'cartItems':cartItems, 'shopping':False}
        else: 
            print("Error")
            messages.error(request, "No se encontro producto")
            return redirect('collections' )
        
    else:
        messages.error(request, "No se encontro categoria")
        return redirect('collections')
    
    return render(request, 'store/products/view.html', context)


#pagina de nosotros
def about(request):
    if request.user.is_authenticated:
        # Obtiene o crea una orden para el usuario actual que aún no esté completa
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        # Obtiene todos los items de la orden
        items = order.orderitem_set.all()
        # Obtiene el total de items en el carrito
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context = {'cartItems':cartItems, 'shopping':False}
    return render(request, 'store/about.html', context)

#carrito
def cart(request):
    # Comprueba si el usuario está autenticado
    if request.user.is_authenticated:
        # Obtiene o crea una orden para el usuario actual que aún no esté completa
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        # Obtiene todos los items de la orden
        items = order.orderitem_set.all()
        # Obtiene el total de items en el carrito
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        print('Carrito:',cart)
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shopping':False}
        cartItems = order['get_cart_items']


        for i in cart:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=i)
            total = (product.selling_price * cart[i]["quantity"])

            order['get_cart_total'] += total
            order['get_cart_items'] * cart[i]["quantity"] 

            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.selling_price,
                    'imageURL':product.imageURL
                },
                'quantity':cart[i]['quantity'],
                'get_cart_total':total
            }

            items.append(item)
            
    products = Product.objects.all()
    # Crea el contexto para la plantilla
    context = {'items':items, 'order':order, 'products':products, 'cartItems':cartItems, 'shopping':False}
    # Renderiza la plantilla con el contexto
    return render(request, 'store/products/cart.html', context)


#pago

def checkout(request):
    # Comprueba si el usuario está autenticado
    if request.user.is_authenticated:
        # Obtiene o crea una orden para el usuario actual que aún no esté completa
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        # Obtiene todos los items de la orden
        items = order.orderitem_set.all()
        # Obtiene el total de items en el carrito
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    # Crea el contexto para la plantilla
    context = {'items':items, 'order':order, 'cartItems':cartItems, 'shopping':False}
    # Renderiza la plantilla con el contexto
    return render(request, 'store/products/checkout.html', context)

#recibe los datos que se guardan al dar clic en los botones de agregar y envia una respuesta al front
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    #imprimimos los datos
    print('Accion:',action)
    print('ProductId:',productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem,created = OrderItem.objects.get_or_create(order=order, product=product)

    #si la accion es agregar, aumentamos la contidad de productos
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)#aumenta la cantidad
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)#disminuye la cantidad
    orderItem.save()#guarga los cambios

    #verifica si la cantidad de productos es igual a 0
    if orderItem.quantity <= 0:
        orderItem.delete()#elimina la orden

    return JsonResponse('Se agrego a carrito',safe=False)

from django.views.decorators.csrf import csrf_exempt
#proceso de orden
@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user#usuario
        order, created = Order.objects.get_or_create(customer=customer, complete=False)#orden
        total = float(data['form']['total'])#precio total
        order.transaction_id = transaction_id#id de la transaccion

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shopping == True:
            ShoppingAdress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode']
            )

    else:
        messages.warning(request,"No has iniciado sesion")

    return JsonResponse('Pago Completado',safe=False)