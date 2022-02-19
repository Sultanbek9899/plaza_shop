from .cart import Cart


def get_context_cart(request):
    '''
    get user cart and send to all templates
    with context processor
    :param request: - request
    :return: - dict
    '''
    cart = Cart(request)
    context = {
        "cart": cart
    }
    return context