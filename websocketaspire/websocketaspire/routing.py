# mysite/routing.py
from channels.routing import ProtocolTypeRouter

# application = ProtocolTypeRouter({
    # (http->django views is added by default)
# })

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import notification.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            notification.routing.websocket_urlpatterns
        )
    ),
})