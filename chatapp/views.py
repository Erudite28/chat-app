from django.shortcuts import redirect, render
from .models import Room,Message

# Create your views here
def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html', {'room': room})

def checkview(request):
    if request.method == 'POST':
        room = request.POST['room_name']
        username = request.POST['username']

        if Room.objects.filter(name=room).exists():
            return redirect('/' +room+ '/?username=' +username)
            #return redirect(f'/room/?username={username}&room={room}') 
        else:
            new_room = Room.objects.create(name=room)
            new_room.save();
            return redirect('/' +room+ '/?username=' +username)
            #return redirect(f'/room/?username={username}&room={room}') 
    else:
        return render(request, 'room.html')
