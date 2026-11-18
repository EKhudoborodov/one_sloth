from django.urls import re_path
from one_sloth import consumers

websocket_urlpatterns = [
    re_path(r'ws/alert/$', consumers.AlertConsumer.as_asgi()),
]