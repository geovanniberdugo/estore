from django.shortcuts import render
from .models import Cart

def cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    
    if cart_id:
        #Get the cart from database
        cart = Cart.objects.get(pk=cart_id
    else:
        #Create the cart from database
        cart = Cart.objects.create(user=user)

    request.session['cart_id'] = cart.id

    return render(request, 'carts/cart.html', {

    })
