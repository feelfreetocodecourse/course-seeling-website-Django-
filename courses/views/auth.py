from django.shortcuts import render
from courses.models import Course , Video
from django.shortcuts import HttpResponse
# Create your views here.

from courses.forms import RegistrationForm


def signup(request ):
    if(request.method == "GET"):
        form = RegistrationForm()
        return  render(request , 
        template_name="courses/signup.html" , context= { 'form' : form } )    
    
    return HttpResponse("POST REQUEST")
    

def login(request ):
    return  render(request , 
    template_name="courses/login.html" )    