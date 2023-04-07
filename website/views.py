
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This is data send from view to template",
                   "user": "USER"})

def date(request):
    return HttpResponse("Page served at " + str(datetime.now()))

def about(request):
    return HttpResponse("I am Abhijeet Gulhane. Software developer by day and Calligrapher by night. ;> ")