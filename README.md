# Cafeteria-Ordering-and-Pickup-System
from main.models import Cafeteria, MenuItem, Order
from django.contrib.auth.models import User
from datetime import date

# Create Cafeteria instances
cafeteria1 = Cafeteria.objects.create(name='Cafeteria 1', location='Building A')
cafeteria2 = Cafeteria.objects.create(name='Cafeteria 2', location='Building B')

# Create User instance (for the order)
user = User.objects.create(username='sample_user', email='user@example.com', password='password')

# Create MenuItem instances
item1 = MenuItem.objects.create(cafeteria=cafeteria1, name='Burger', description='Delicious burger', price=5.99, is_vegetarian=False, is_vegan=False, is_gluten_free=False)
item2 = MenuItem.objects.create(cafeteria=cafeteria1, name='Salad', description='Healthy salad', price=3.99, is_vegetarian=True, is_vegan=True, is_gluten_free=True)
item3 = MenuItem.objects.create(cafeteria=cafeteria2, name='Pizza', description='Classic pizza', price=8.99, is_vegetarian=False, is_vegan=False, is_gluten_free=False)

# Create Order instances
order1 = Order.objects.create(user=user, cafeteria=cafeteria1, order_number='123456', status='pending', total_amount=0.0, dining_preference='takeout', day=date.today())
order2 = Order.objects.create(user=user, cafeteria=cafeteria2, order_number='789012', status='pending', total_amount=0.0, dining_preference='dine-in', day=date.today())

# Add items to orders using OrderItem
order1.items.add(item1, through_defaults={'quantity': 2})
order1.items.add(item2, through_defaults={'quantity': 1})
order2.items.add(item3, through_defaults={'quantity': 1})
