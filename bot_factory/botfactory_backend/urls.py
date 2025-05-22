from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/bots/", include("bots.urls")),
    path("api/v1/chats/", include("chats.urls")),
    path("api/v1/webhook/", include("webhook.urls")),
]

if settings.DEBUG:
    from drf_spectacular.views import (
        SpectacularSwaggerView,
    )

    urlpatterns += [
        path(
            "api/v1/docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]
