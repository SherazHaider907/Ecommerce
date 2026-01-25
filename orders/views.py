from datetime import date
from django.shortcuts import redirect, render
from carts.models import CartItem
from .models import Order
from .forms import OrderForm


def place_order(request, total=0, quantity=0):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()

    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0

    for cart_item in cart_items:
        total = cart_item.product.price * cart_item.quantity
        grand_total += total

    tax = (2 * grand_total) / 100
    grand_total += tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = request.user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # Order number
            today = date.today()
            current_date = today.strftime("%Y%m%d")
            data.order_number = current_date + str(data.id)
            data.is_ordered = True
            data.save()

            return redirect('checkout')

        # ✅ VERY IMPORTANT: form invalid case
        return redirect('checkout')

# def payments(request):
#     return render(request, 'orders/payments.html')

# def order_complete(request):
#     return render(request, 'orders/order_complete.html')