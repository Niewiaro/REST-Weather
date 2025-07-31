from django.http import HttpResponse


def healthz(request):
    """
    Health check endpoint.
    """
    return HttpResponse("OK", status=200)
