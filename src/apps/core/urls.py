from django.urls import path
from .views.system import healthz, version, info

urlpatterns = [
    path("healthz/", healthz, name="healthz"),
    path("version/", version, name="version"),
    path("info/", info, name="info"),
]
