from django.urls import path
from .views import browse_menus, place_order, order_history, track_order, attendance,pickup_order,home

urlpatterns = [
    path('browse_menus/', browse_menus, name='browse_menus'),
    path('place_order/<int:cafeteria_id>/', place_order, name='place_order'),
    path('order_history/', order_history, name='order_history'),
    path('track_order/<str:order_id>/', track_order, name='track_order'),
    path('attendance/', attendance, name='attendance'),
    path('pickup_order/<int:order_id>/', pickup_order, name='pickup_order'), 
    path('', home, name='home'), 

]
