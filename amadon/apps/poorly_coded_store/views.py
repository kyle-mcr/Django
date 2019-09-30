from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request, order_id):
    total = 0
    orders = Order.objects.all()
    for order in orders:
        total += order.total_price  
    context = {
        'order': Order.objects.get(id=order_id),
        'ordernum': Order.objects.last(),
        'total': total
    }

    return render(request, "store/checkout.html", context)
 
def order(request):
    product = Product.objects.get(id=request.POST['product'])
    quantity = int(request.POST['quantity'])
    total = product.price * quantity
    new_order = Order.objects.create(quantity_ordered=quantity, total_price=total)
    new= new_order.id
    return redirect('/checkout/{}'.format(new))