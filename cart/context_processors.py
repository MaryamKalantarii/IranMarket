from .cart import CartSession
from.models import CartItemModel
# def cart_processor(request):
#     cart = CartSession(request.session)
#     return{"cart": cart}






def cart_processor(request):
    cart = CartSession(request.session)
    return {
        "cart": cart,
        "cart_items": cart.get_cart_items(),
        "total_quantity": cart.get_total_quantity(),
        "total_payment": cart.get_total_payment_amount(),
    }