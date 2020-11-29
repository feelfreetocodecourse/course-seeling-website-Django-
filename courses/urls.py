
from django.contrib import admin
from django.urls import path , include
from courses.views import home , coursePage , SignupView , LoginView , signout , checkout
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', home , name = 'home'),
    path('logout', signout , name = 'logout'),
    path('signup', SignupView.as_view() , name = 'signup'),
    path('login', LoginView.as_view() , name = 'login'),
    path('course/<str:slug>', coursePage , name = 'coursepage'),
    path('check-out/<str:slug>', checkout , name = 'checkpage'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)