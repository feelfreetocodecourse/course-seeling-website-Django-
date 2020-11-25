from django.shortcuts import render
from courses.models import Course , Video
from django.shortcuts import HttpResponse
# Create your views here.


def signup(request ):
    return  render(request , 
    template_name="courses/signup.html" )    

def login(request ):
    return  render(request , 
    template_name="courses/login.html" )    