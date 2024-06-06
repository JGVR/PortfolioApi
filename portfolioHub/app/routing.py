from django.urls import path
from .routes import chat_bot

websocket_urlpatterns = [
    path("ws/chat/", chat_bot.ChatBotConsumer.as_asgi())
]