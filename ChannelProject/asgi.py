import os
import ChannelApp.routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChannelProject.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        SessionMiddlewareStack(URLRouter(
            ChannelApp.routing.websocket_urlpatterns  # Ensure this matches your routing.py
        ))
    ),
})



