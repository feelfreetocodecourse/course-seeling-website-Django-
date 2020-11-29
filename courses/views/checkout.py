from django.shortcuts import render , redirect
from courses.models import Course , Video
from django.shortcuts import HttpResponse
# Create your views here.

def checkout(request , slug):
    course = Course.objects.get(slug  = slug)
   
    if not request.user.is_authenticated:
        return redirect("login")
        # i you are enrooled in this course you can watch every video

    context = {
        "course" : course , 
    }
    return  render(request , template_name="courses/check_out.html" , context=context )    
    