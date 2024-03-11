from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cafeteria, MenuItem, Order, OrderItem
import uuid
from django.core.mail import send_mail


def browse_menus(request):
    cafeterias = Cafeteria.objects.all()
    menu_items = MenuItem.objects.all()
    context = {'cafeterias': cafeterias, 'menu_items': menu_items}
    return render(request, 'browse_menus.html', context)


@login_required
def place_order(request, cafeteria_id):
    cafeteria = get_object_or_404(Cafeteria, id=cafeteria_id)
    menu_items = MenuItem.objects.filter(cafeteria=cafeteria)
    zipped_list={}
    if request.method == 'POST':
        # Extract form data and create the order
        selected_items = request.POST.getlist('selected_items')
        dining_preference = request.POST.get('dining_preference')
        pickup_location = request.POST.get('pickup_location')  # Added pickup_location
        print( selected_items )
        # Generate a unique order number
        order_number = str(uuid.uuid4())[:8]

        order = Order.objects.create(user=request.user, cafeteria=cafeteria,
                                     order_number=order_number, dining_preference=dining_preference,status='pending')

        total_amount = 0  # Initialize total_amount
        orders = []
        quan = []
        for item_id in selected_items:
            menu_item = MenuItem.objects.get(pk=item_id)
            quantity = request.POST.get(f'quantity_{item_id}', 0)
            order_item = OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)

            orders.append(menu_item.name)
            quan.append(quantity)
            
            total_amount += menu_item.price * int(quantity)
        

        order.total_amount = total_amount
        order.save()
        zipped_list = zip(orders, quan)
        

        messages.success(request, 'Order placed successfully!')
        return redirect('order_history')

    context = {'cafeteria': cafeteria, 'menu_items': menu_items,'zipped_list': zipped_list}
    return render(request, 'place_order.html', context)

from .utils import sendmail
@login_required
def pickup_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status != 'picked_up':
        order.status = 'picked_up'
    else:
        messages.warning(request, 'This order has already been picked up.')
    order.save()

    sendmail(order,request)

    messages.success(request, 'Order picked up successfully. Check your email for details.')

    return redirect('order_history')

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'order_history.html', context)

@login_required
def track_order(request, order_id):
    #order = Order.objects.get(order_number=order_id, user=request.user)
    order = get_object_or_404(Order, order_number=order_id, user=request.user)

    context = {'order': order}
    return render(request, 'track_order.html', context)

@login_required
def attendance(request):
    # Logic 
    return render(request, 'attendance.html')
