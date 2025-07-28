from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from datetime import datetime, timezone
import platform

START_TIME = datetime.now(timezone.utc)


@api_view(["GET"])
@permission_classes([AllowAny])
def healthz(request):
    return Response({"status": "ok"})


@api_view(["GET"])
@permission_classes([AllowAny])
def version(request):

    return Response(
        {
            "version": "1.0.0",
            "python": platform.python_version(),
        }
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def info(request):
    uptime = datetime.now(timezone.utc) - START_TIME
    return Response(
        {
            "app": "REST Weather",
            "system": platform.system(),
            "hostname": platform.node(),
            "uptime": str(uptime),
        }
    )
