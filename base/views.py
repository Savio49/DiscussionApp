from django.shortcuts import render

from .models import Room
from .forms import RoomForm

# queryset = ModelName.objects.all() # objects is the model manager which gives access to methods like all(), get(), filter(), exclude()

# rooms = [
#     {'id': 1, 'name': 'Room 1'},
#     {'id': 2, 'name': 'Room 2'},
#     {'id': 3, 'name': 'Room 3'},
# ]


def home(request):
    rooms = Room.objects.all()  # query to get all rooms. objects is the model manager
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)  # query data using id
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm
    context = {'form':form}
    return render(request, 'base/room_form.html', context)

# Class based views are faster and easier to work with instead of function based views. But they get complicated for larger projects. We stick to function based views for understanding MODEL-FORMS
