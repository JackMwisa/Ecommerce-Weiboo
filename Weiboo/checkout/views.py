from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order
from uuid import uuid4

@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user, status='active').first()
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address')
        billing_address = request.POST.get('billing_address')

        order = Order.objects.create(
            user=request.user,
            cart=cart,
            order_number=str(uuid4()).split('-')[0].upper(),
            shipping_address=shipping_address,
            billing_address=billing_address,
            total_price=cart.total_price,
        )

        cart.status = 'checked_out'
        cart.save()

        return redirect('checkout_success')

    return render(request, 'checkout/checkout.html')

@login_required
def checkout_success(request):
    return render(request, 'checkout/success.html')
