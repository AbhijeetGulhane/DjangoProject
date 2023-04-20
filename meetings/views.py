from django.shortcuts import render, get_object_or_404, redirect
# from django.forms import modelform_factory

from .models import Meeting, Room
from .forms import MeetingForm, RoomForm


def detail(request, m_id):
    meeting = get_object_or_404(Meeting, pk=m_id)
    # meeting = Meeting.objects.get(pk=m_id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def detail_room(request, r_id):
    room = get_object_or_404(Room, pk=r_id)
    return render(request, "meetings/detail_room.html", {"room": room})


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


# As a bonus, here are example implementations
# Of an edit and delete form
# See also urls.py and templates

def edit(request, id):
    # First, get the meeting to edit from the database
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        # After editing: get data from form
        # Note the second argument: the meeting we are editing
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            # redirect back to detail page after save
            return redirect("detail", id)
    else:
        # Pre-fill the form with data from existing meeting
        form = MeetingForm(instance=meeting)
    return render(request, "meetings/edit.html", {"form": form})


def edit_room(request, id):
    room = get_object_or_404(Room, pk=id)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("detail_room", id)
    else:
        form = RoomForm(instance=room)
    return render(request, "meetings/edit_room.html", {"form": form})


# Delete is different: the form is only shown to ask for confirmation
# When we get a POST, we know we can go ahead and delete
def delete(request, id):
    # First, get the meeting to edit from the database
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("home")
    else:
        return render(request, "meetings/confirm_delete.html", {"meeting": meeting})
