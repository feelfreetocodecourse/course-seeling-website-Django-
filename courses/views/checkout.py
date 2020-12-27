from django.shortcuts import render , redirect
from courses.models import Course , Video , Payment
from django.shortcuts import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from codewithvirendra.settings import *
from time import time
import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

def checkout(request , slug):
    course = Course.objects.get(slug  = slug)
    user = None
    if not request.user.is_authenticated:
        return redirect("login")
        # i you are enrooled in this course you can watch every video
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    if action == 'create_payment':
        amount =  int((course.price - ( course.price * course.discount * 0.01 )) * 100)
        currency = "INR"
        notes = {
            "email" : user.email, 
            "name" : f'{user.first_name} {user.last_name}'
        }
        reciept = f"codewithvirendra-{int(time())}"
        order = client.order.create(
            {'receipt' :reciept , 
            'notes' : notes , 
            'amount' : amount ,
            'currency' : currency
            }
        )

        payment = Payment()
        payment.user  = user
        payment.course = course
        payment.order_id = order.get('id')
        payment.save()

    context = {
        "course" : course , 
        "order" : order, 
        "payment" : payment, 
        "user" : user
    }
    return  render(request , template_name="courses/check_out.html" , context=context )    


@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        try:
            client.utility.verify_payment_signature(data)
            return render(request , template_name="courses/my_courses.html" , context=context)    

        except:
            return HttpResponse("Invalid Payment Details")
        
        
 
