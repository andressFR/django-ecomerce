
/*Funcion para hacer funcionar los botones de cantidad de productos (+ y -)*/
$(document).ready(function () {
    //funcion para el boton de aumento
    $('.increment-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;

        /* Si el valor llega a 10 no permitira seguir aumentando l cantidad */
        if (value < 10) {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    })

    //funcion para el boton de decremento
    $('.decrement-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;

        /* Si el valor le 1 no permitira seguir disminuyendo la cantidad */
        if (value > 1) {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    //agregar al carrito
    /* $('.addToCartBtn').click(function(e){
         e.preventDefault();
     
         //id del producto
         var product_id = $(this).closest('.product_data').find('.prod_id').val();
     
         //Cantidad de productos
         var product_qty = $(this).closest('.product_data').find('.qty-input').val();
     
         var token = $('input[name=csrfmiddlewaretoken]').val();
     
         $.ajax({
             type: "POST",
             url: "/add-to-cart",
             data: {
                 'product_id': product_id,
                 'product_qty': product_qty,
                 'csrfmiddlewaretoken': token
             },
             success: function (response) {
                 console.log(response);
             }
         });
     });*/

});

