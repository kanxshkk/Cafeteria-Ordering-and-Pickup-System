from django.db import models
from django.contrib.auth.models import User

class Cafeteria(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class MenuItem(models.Model):
    cafeteria = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_vegetarian = models.BooleanField()
    is_vegan = models.BooleanField()
    is_gluten_free = models.BooleanField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafeteria = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('preparing', 'Preparing'), ('ready', 'Ready'), ('picked_up', 'Picked Up')])
    items = models.ManyToManyField(MenuItem, through='OrderItem', related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    dining_preference = models.CharField(max_length=10, choices=[('dine-in', 'Dine-In'), ('takeout', 'Takeout')])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dietary_preference = models.CharField(max_length=20, choices=[('vegetarian', 'Vegetarian'), ('vegan', 'Vegan'), ('gluten_free', 'Gluten-Free')])

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafeteria = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
