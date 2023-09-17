from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext as _

class Cart:
    """
    Initial Cart
    """
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            self.session['cart'] = {}
            cart = self.session['cart']

        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['count'] * item['product_obj'].price
            yield item

    def __len__(self):
        return len(self.cart)

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        return sum(item['count'] * item['product_obj'].price for item in self.cart.values())

    def add(self, product, count=1, replace_current_count=False):
        """
        Add Product To Cart
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'count': 0}
        if replace_current_count:
            self.cart[product_id]['count'] = count
        else:
            self.cart[product_id]['count'] += count
        self.save()

        messages.success(self.request, _('the product successfully added to cart'))

    def delete(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        messages.success(self.request, _('the product successfully deleted from cart'))


    def save(self):
        # self.session['total'] = sum(i['count'] * i['price'] for i in self.cart.values())
        self.session.modified = True
