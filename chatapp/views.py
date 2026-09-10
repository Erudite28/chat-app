from django.shortcuts import redirect, render
from .models import Room,Message
from django.contrib import messages

# Create your views here
def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html')

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        messages.info(request, 'room already exists')
        return redirect('/' +room+ '/?username=' +username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save();
        return redirect('/' +room+ '/?username=' +username)