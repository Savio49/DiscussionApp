from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        # return a user if it exists else returns none
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # adds the session in the database and the browser (as a cookie)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username and password does not match')
    context = {}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)  # deletes the session token
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
                                Q(name__icontains=q) |
                                Q(description__icontains=q) |
                                Q(host__username__icontains=q)
                                )

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
