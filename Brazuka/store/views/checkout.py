from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        date_delivery = request.POST.get('date_delivery')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        
        if len(address) > 0 and len(date_delivery) > 0:

            for product in products:
                order = Order(customer=Customer(id=customer),
                              product=product,
                              price=product.price,
                              address=address,
                              date_delivery=date_delivery,
                              quantity=cart.get(str(product.id)))
                order.save()

            request.session['cart'] = {}


        return redirect('cart')
