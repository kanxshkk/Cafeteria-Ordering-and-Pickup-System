
from django.core.mail import send_mail

def sendmail(order,request):
    
    subject = 'Your Order has been Picked Up'
    message = f'Thank you for picking up your order!\n\nOrder Number: {order.order_number}'
    from_email = 'kanishkakash514@gmail.com' 
    recipient_list = [request.user.email]

    send_mail(subject, message, from_email, recipient_list)
    print("mail sent")
    