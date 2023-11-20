//variable que guarda el boton de agregar
var updateBtns = document.getElementsByClassName('update-cart');

//ciclo que recorre la longitud de los botones
for (var i = 0; i < updateBtns.length; i++) {
    //evento de los botones de agregar
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;//id del producto
        var action = this.dataset.action;//accion de agrear (add)

        console.log('productId: ', productId, 'action: ', action);
        console.log('USER: ', user)

        if (user === 'AnonymousUser') {
            addCookieItem(productId, action);
        } else {
            updateUserOrder(productId, action);

            alertify.set('notifier', 'position', 'top-center');
            alertify.success('Prodducto Agregado');
        }

    });
}

//Funcion para agregar a carrito cuanddo el usuario no esta autenticado
function addCookieItem(productId, action) {
    console.log('No has iniciado sesion');

    //agregar
    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity': 1 }
        } else {
            cart[productId]['quantity'] += 1
        }
    }

    //eliminar
    if (action == 'remove') {
        cart[productId]['quantity'] += 1

        if (cart[productId]['quantity'] <= 0) {
            console.log('Producto eliminado')
            delete cart[productId]
        }
    }

    console.log('Carrito:', cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
    location.reload();

}

/*NO LE ENTIENDO A JAVASCRIPT */

//Funcion para agregar a carrito cuanddo el usuario esta autenticado
function updateUserOrder(productId, action) {
    console.log('El usuario a iniciado sesion');

    var url = '/update_item/';

    //api de recuperacion de datos
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'applicartion/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

        //respuesta del backend
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
}