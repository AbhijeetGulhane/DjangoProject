from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting


# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"username": "USER",
                   "num_meetings": Meeting.objects.count()})


def date(request):
    return HttpResponse("Page served at " + str(datetime.now()))


def about(request):
    return HttpResponse("I am Abhijeet Gulhane. Software developer by day and Calligrapher by night. ;> ")
