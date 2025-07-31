from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from datetime import datetime, timezone
from django.conf import settings
import platform

START_TIME = datetime.now(timezone.utc)


@api_view(["GET"])
@permission_classes([AllowAny])
def healthz_api(request):
    result = {"status": "ok"}
    return Response(result)


@api_view(["GET"])
@permission_classes([AllowAny])
def version(request):
    result = {
        "version": settings.APP_VERSION,
        "python": platform.python_version(),
    }

    return Response(result)


def get_database_info():
    from django.db import connection

    engine = connection.settings_dict.get("ENGINE", "unknown")
    vendor = connection.vendor

    version = "unknown"
    with connection.cursor() as cursor:
        try:
            if vendor == "sqlite":
                cursor.execute("select sqlite_version()")
                version = cursor.fetchone()[0]
            elif vendor == "postgresql":
                cursor.execute("select version()")
                version = cursor.fetchone()[0]
            elif vendor == "mysql":
                cursor.execute("select version()")
                version = cursor.fetchone()[0]
        except Exception:
            pass

    result = {
        "engine": engine,
        "vendor": vendor,
        "version": version,
    }

    return result


@api_view(["GET"])
@permission_classes([AllowAny])
def info(request):
    uptime = datetime.now(timezone.utc) - START_TIME
    db_info = get_database_info()

    result = {
        "app": settings.APP_NAME,
        "system": platform.system(),
        "hostname": platform.node(),
        "uptime": str(uptime),
        "database": get_database_info(),
    }

    return Response(result)
