from django.shortcuts import render, get_object_or_404, redirect
# from django.forms import modelform_factory

from .models import Meeting, Room
from .forms import MeetingForm


def detail(request, m_id):
    meeting = get_object_or_404(Meeting, pk=m_id)
    # meeting = Meeting.objects.get(pk=m_id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


# Please add a new page that shows a list of all room objects
# (Just text, no link)
# Create:- View - Template - URL mapping

def rooms_list(request):
    return render(request, "meetings/room_list.html",
                  {"rooms": Room.objects.all()})


# MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == "POST":  # form has been submitted, process data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  # django will send the browser the view function page and display it to the user
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
