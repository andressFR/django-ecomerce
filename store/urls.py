from django.urls import path
from store import views
from store.controller import authview,cart

"""Archivo en el que se almacenan las urls de la aplicacion"""

urlpatterns = [
    #principales
    path('',views.home, name="home"),#pagina principal
    path('collections',views.collections, name="collections"),#pagina de categorias
    path('collections/<str:slug>',views.collectionsViews, name="collectionsview"),#pagina de una categoria en especifico
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview, name="productview"),#pagina de detalles de producto
    
    #usuarios
    path('register/',authview.register, name="register"),
    path('login/',authview.loginpage, name="loginpage"),
    path('logout/',authview.logoutpage, name="logout"),

    #carrito
    path('add-to-cart',cart.addtocart, name="addtocart"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/',views.processOrder, name="process_order"),

    path('cart',views.cart, name="cart"),
    path('checkout/',views.checkout, name="checkout"),



    #personal
    path('about/',views.about, name="about"),
]