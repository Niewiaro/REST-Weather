from django.urls import path
from .views.system import healthz_api, version, info

urlpatterns = [
    path("healthz/", healthz_api, name="healthz-api"),
    path("version/", version, name="version"),
    path("info/", info, name="info"),
]
