from django.shortcuts import render, redirect

from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q

# queryset = ModelName.objects.all() # objects is the model manager which gives access to methods like all(), get(), filter(), exclude()


def home(request):
    # .filter() works like .all(), topic__name comes from attributes of Room model. That works but except for 'All' filter
    # q = request.GET.get('q')
    # rooms = Room.objects.filter(topic__name=q) # Doesn't work for 'All'

    # 'q' is the name of input form in navbar.html
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # filter works if the query contains atleast some part of the string. i makes the case-insensitive. other parameters which may be used: startswith, endswith etc
    # rooms = Room.objects.filter(topic__name__icontains=q) # This only searches by topic__name. Not by user or room name. How to make it dynamic?
    # rooms = Room.objects.filter(topic__name__icontains=q, name__contains=q) # Not a good way. Instead use django's QLookup method to add AND/OR statements in searches
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
                                Q(name__icontains=q) |
                                Q(description__icontains=q) |
                                Q(host__username__icontains=q)
                                )

    # alternatively use len(rooms). But this works faster cuz specially for sql queries
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj', room})

    #     form = RoomForm(request.POST, instance=room)
    # form = RoomForm(instance=room)


# Class based views are faster and easier to work with instead of function based views. But they get complicated for larger projects. We stick to function based views for understanding MODEL-FORMS
