from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

from .models import Meeting, Room


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start': TimeInput(attrs={"type": "time"}),
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "60"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meetings cannot be in the past")
        return d


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'name': DateInput(attrs={"type": "string"}),
            'floor': TimeInput(attrs={"type": "number", "min": "1", "max": "4"}),
            'room_number': TextInput(attrs={"type": "number", "min": "1", "max": "1080"})
        }
