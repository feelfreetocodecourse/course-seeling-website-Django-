from django.shortcuts import render , redirect
from courses.models import Course , Video
from django.shortcuts import HttpResponse
# Create your views here.
from courses.forms import RegistrationForm
from django.views import View


class SignupView(View):
    def get(self , request):
        form = RegistrationForm()
        print("Respinse form Class Based")
        return render(request , 
        template_name="courses/signup.html" , context= { 'form' : form } ) 
    
    def post(self , request):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            if(user is not None):
                return redirect('login')
        return render(request , 
            template_name="courses/signup.html" , context= { 'form' : form } )
    
    

def login(request ):
    return  render(request , 
    template_name="courses/login.html" )    