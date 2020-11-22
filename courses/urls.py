
from django.contrib import admin
from django.urls import path , include
from courses.views import home , coursePage
from django.conf.urls.static import static
from codewithvirendra.settings import MEDIA_ROOT , MEDIA_URL
urlpatterns = [
    path('', home , name = 'home'),
    path('course/<str:slug>', coursePage , name = 'coursepage'),
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
