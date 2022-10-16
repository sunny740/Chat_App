"""
ASGI config for Chat_App project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import chat.routing

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
  "http": django_asgi_app,
  "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    ),
})


# import os
# import chat.routing

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter,URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.core.asgi import get_asgi_application
# from .urls import ws_patterns

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat_App.settings')
# django_asgi_app = get_asgi_application()

# # application = get_asgi_application()

# routes = URLRouter(ws_patterns)

# application = ProtocolTypeRouter({

#     # "http": get_asgi_application(),
#     # "websocket": routes
#     "http": django_asgi_app,
#     "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 chat.routing.websocket_urlpatterns
#             )
#         )
#     ),
# })