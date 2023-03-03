from django.urls import path
from .views import (
    room, checkview, send, getMessages,
    HomePageView, ChatRoomPageView, ChatBotPageView
    )

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("chat-bot/", ChatBotPageView.as_view(), name="chat-bot"),
    path('chat-room/', ChatRoomPageView.as_view(), name='chat-room'),
    path('<str:room>/', room, name='room'),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
]
