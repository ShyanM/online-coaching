from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('programs'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K6ClXE8mmCVFCybRHay7YMBnYEonkWGpEHc7cZLiAsa7ehuxxNV24YfOVdMCRLEMPz81sPN6z0qTynYvymdRnkr00luPaIGLe',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)