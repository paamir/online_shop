from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .cart import Cart
from products.models import Product
from .forms import AddToCartProductForm


def cart_details_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_count_form'] = AddToCartProductForm(
            initial={
                'count': item['count'],
                'inplace': True
            }

        )
    return render(request, 'cart/cart_detail.html', context={
        'cart': cart,
    })


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        count = cleaned_data['count']
        cart.add(product, count, cleaned_data['inplace'])
    return redirect('cart_details')


def delete_from_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    cart.delete(product)
    return redirect('cart_details')
