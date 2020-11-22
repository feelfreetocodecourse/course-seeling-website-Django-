from django.shortcuts import render
from courses.models import Course
from django.shortcuts import HttpResponse
# Create your views here.


def home(request):
    courses = Course.objects.all()
    print(courses)
    return render(request , template_name="courses/home.html" , context={"courses" : courses} )