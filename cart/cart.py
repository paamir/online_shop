from products.models import Product
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
            cart[str(product.id)]['product_obj'] = products

        for item in cart.values():
            yield item

    def __len__(self):
        return len(self.cart)

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return sum(product.price for product in products)

    def Add(self, product, price, count=1):
        """
        Add Product To Cart
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'count': count, 'price': price}
        else:
            self.cart[product_id]['count'] += count
        self.save()

    def Delete(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # self.session['total'] = sum(i['count'] * i['price'] for i in self.cart.values())
        self.session.modified = True
