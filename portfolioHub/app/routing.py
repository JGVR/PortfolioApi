from django.urls import path
from .routes import chat_bot_consumer

websocket_urlpatterns = [
    path("ws/chat/", chat_bot_consumer.ChatBotConsumer.as_asgi())
]