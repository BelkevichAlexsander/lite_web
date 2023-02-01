from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .exceptions import NoElementsInVersionControl

ERROR_MISTAKE_INDEX = 'No versions present. Please check if the input is correct.'
version_control = []


@csrf_exempt
def version(request):
    try:
        if request.method == 'GET':
            if not version_control:
                raise NoElementsInVersionControl

            return JsonResponse(version_control, safe=False)

        elif request.method == 'POST':
            version_control.append({
                'id': str(len(version_control)),
                'software': request.POST.get('software'),
                'version': request.POST.get('version')
            })

            return JsonResponse({'Create': version_control[len(version_control) - 1]})
    except NoElementsInVersionControl as error:
        return JsonResponse({'ERROR': str(error)})


def one_version(request, lite_pk):
    try:
        if request.method == 'GET':
            return JsonResponse({'Selected version': version_control[lite_pk]})
    except IndexError:
        return JsonResponse({'ERROR': ERROR_MISTAKE_INDEX})


@csrf_exempt
def correct(request, lite_pk):
    try:
        if request.method == 'POST':
            version_control[lite_pk] = {
                'id': str(lite_pk),
                'software': request.POST.get('software'),
                'version': request.POST.get('version')
            }

            return JsonResponse({'Update': version_control[lite_pk]})
    except IndexError:
        return JsonResponse({'ERROR': ERROR_MISTAKE_INDEX})


@csrf_exempt
def delete(request, lite_pk):
    try:
        if request.method == 'POST':
            version_control[lite_pk] = {
                'id': str(lite_pk),
                'software': None,
                'version': None
                }

            return JsonResponse({'Delete': version_control[lite_pk]})
    except IndexError:
        return JsonResponse({'ERROR': ERROR_MISTAKE_INDEX})
