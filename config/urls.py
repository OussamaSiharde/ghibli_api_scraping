from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.urls import include, path

from ghibli_core.movie import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title="ghibli app API", default_version="v1",),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    url(
        r"^$",
        lambda request: HttpResponse(
            "Yes I am alive!!!", content_type="application/json"
        ),
        name="ping",
    ),
    path("movies/", views.MovieListView.as_view(), name="movies"),
    path("api/", include("config.api_urls")),
    path("admin/", admin.site.urls),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
