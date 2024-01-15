from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
import stripe
from store.models.product import Products
from store.models.orders import Order
from django.conf import settings
stripe.api_key = 'sk_test_51OVhvjHlLWKVaiHGSyIOeqWvfPUsQOHP6Mxsqd2rorZithyb1a63fx7CGecpKtlFkXHCEVpQdiR3ujuSFNjveTMC00U94rU3h0'
class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))

        print(address, phone, customer, cart, products)

        line_items = []

        for product in products:
            quantity = cart.get(str(product.id))
            unit_amount = int(product.price) * 100

            line_items.append({
                'price_data': {
                    'currency': 'usd',  # Change to your desired currency
                    'unit_amount': unit_amount,
                    'product_data': {
                        'name': product.name,
                        'images': [
                            f"http://rak5ha5a.pythonanywhere.com/{product.image.url}"
                        ],
                    },
                },
                'quantity': quantity,
            })

            order = Order(
                customer=Customer(id=customer),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=quantity
            )
            order.save()

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url='http://rak5ha5a.pythonanywhere.com/success/',  # Change to your success URL
            cancel_url='http://rak5ha5a.pythonanywhere.com/cancel/',  # Change to your cancel URL
        )

        request.session['cart'] = {}

        return redirect(checkout_session.url)
