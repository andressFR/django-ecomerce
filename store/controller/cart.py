from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
#import json

from store.models import Product,Cart

def addtocart(request):
    #verifica si el mettodo de envio es POST
    if request.method == 'POST':
        #Verifica si el usuario esta autenticado
        if request.user.is_authenticated:
            #Id del producto
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)

            #Verifica que el producto este registrado
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "Se envio a carrito"})
                else:
                    #Cantidad de productos
                    prod_qty = int(request.POST.get('product_qty'))

                    #verifica si la ccantidades disponibles es mayor a los productos agregados
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Producto agregado correctamente"})
                    else:
                        return JsonResponse({'status':"Solo" + str(product_check.quantity) + "Cantidades Disponible"})
                    
            return JsonResponse({'status': "No se encontro producto"})
        #En caso de no estar autenticado pedimos iniciar sesion a usuario
        else:
            return JsonResponse({'status': "Inicia Sesion Para Continuar"})

    return redirect('/')
    