from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from django.views.generic import TemplateView
from .models import Room, Message


# Create your views here.
class HomePageView(TemplateView):   
    template_name = "home.html"

class ChatBotPageView(TemplateView):   
    template_name = "chat_home_bot.html"

class ChatRoomPageView(TemplateView):   
    template_name = "chat_home_room.html"

def room(request, room):
    username = request.GET.get('username')
    room_details = get_object_or_404(Room, name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    room_query, created = Room.objects.get_or_create(name=room)
    url = reverse('room', args=(room,))
    return redirect(url + '?username=' + request.POST['username'])

def send(request):
    post_data = request.POST
    Message.objects.create(value=post_data['message'], user=post_data['username'], room=post_data['room_id'])
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = get_object_or_404(Room, name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})