from django.shortcuts import render, get_object_or_404

from .models import Meeting


def detail(request, m_id):
    meeting = get_object_or_404(Meeting, pk=m_id)
    # meeting = Meeting.objects.get(pk=m_id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

