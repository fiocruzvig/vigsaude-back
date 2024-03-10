from django.http import HttpResponse
from django.http import JsonResponse



def require_post(function):
    def wrapped_view(request, *args, **kwargs):
        if request.method != 'POST':
            return HttpResponse(JsonResponse({"Status":"Método Inválido"}), content_type="application/json", status=405)
        return function(request, *args, **kwargs)
    return wrapped_view