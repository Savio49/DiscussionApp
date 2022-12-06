from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # or specify a list of attributes of Room in a list. Eg. ['name', 'description']
        fields = '__all__'
