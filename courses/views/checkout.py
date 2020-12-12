from django.shortcuts import render , redirect
from courses.models import Course , Video
from django.shortcuts import HttpResponse
# Create your views here.
from codewithvirendra.settings import *

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
    if action == 'create_payment':
        amount =  int((course.price - ( course.price * course.discount * 0.01 )) * 100)
        currency = "INR"
        notes = {
            "email" : user.email, 
            "name" : f'{user.first_name} {user.last_name}'
        }  

    context = {
        "course" : course , 
        "order" : order
    }
    return  render(request , template_name="courses/check_out.html" , context=context )    
    