import json

from django.http.response import JsonResponse
from django.views.generic import RedirectView

ERROR_MISTAKE_INDEX = 'No versions present. Please check if the input is correct.'
VERSION_CONTROL = []


class VersionView(RedirectView):
    def get(self, request, *args, **kwargs):
        if len(kwargs):
            return JsonResponse(VERSION_CONTROL[kwargs["pk"]])
        return JsonResponse(VERSION_CONTROL, safe=False)

    def post(self, request, *args, **kwargs):
        VERSION_CONTROL.append({
            'id': str(len(VERSION_CONTROL)),
            'software': request.POST.get('software'),
            'version': request.POST.get('version')
        })

        return JsonResponse(VERSION_CONTROL[len(VERSION_CONTROL) - 1])

    def put(self, request, *args, **kwargs):
        answer = json.loads(request.body.decode('utf-8'))

        VERSION_CONTROL[kwargs["pk"]] = {
            'id': str(kwargs["pk"]),
            'software': answer.get('software'),
            'version': answer.get('version')
        }

        return JsonResponse(VERSION_CONTROL[kwargs["pk"]], safe=False)

    def delete(self, request, *args, **kwargs):
        VERSION_CONTROL[kwargs["pk"]] = {
            'id': str(kwargs["pk"]),
            'software': None,
            'version': None
        }

        return JsonResponse(VERSION_CONTROL[kwargs["pk"]], safe=False)
