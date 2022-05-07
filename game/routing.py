from django.urls import path

from game.consumers import WSConsumer

ws_urlpatterns = [
    path('ws/url/', WSConsumer.as_asgi())
]