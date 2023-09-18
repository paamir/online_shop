from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from products.models import Product
from .forms import OrderForm
from .models import OrderItem


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:

        return redirect('product_list')
    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = get_object_or_404(Product, id=item['product_obj'].id)
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    count=item['count'],
                    price=product.price,
                )
            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()


    return render(request, 'orders/order_create.html', context={'form': order_form})
