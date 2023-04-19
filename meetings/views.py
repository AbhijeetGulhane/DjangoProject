from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room


def detail(request, m_id):
    meeting = get_object_or_404(Meeting, pk=m_id)
    # meeting = Meeting.objects.get(pk=m_id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


# Please add a new page that shows a list of all room objects
# (Just text, no link)

# Create:
#   - View
#   - Template
#   - URL mapping

def rooms_list(request):
    return render(request, "meetings/room_list.html",
                  {"rooms": Room.objects.all()})
