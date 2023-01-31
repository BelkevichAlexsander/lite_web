from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .execptions import NotElementsInVersionControl

version_control = []


@csrf_exempt
def version(request):
    try:
        if request.method == 'GET':
            if not version_control:
                raise NotElementsInVersionControl

            return JsonResponse(version_control, safe=False)

        elif request.method == 'POST':
            version_control.append({
                'id': str(len(version_control)),
                'software': request.POST.get('software'),
                'version': request.POST.get('version')
            })

            return JsonResponse({'Create': f'{version_control[len(version_control) - 1]}'})
    except (IndexError, NotElementsInVersionControl) as error:
        return JsonResponse({'ERROR': f'{error}'})


def one_version(request, lite_pk):
    try:
        if request.method == 'GET':
            return JsonResponse({'Selected version': f'{version_control[lite_pk]}'})
    except IndexError as error:
        return JsonResponse({'ERROR': f'{error}'})


@csrf_exempt
def correct(request, lite_pk):
    try:
        if request.method == 'POST':
            version_control[lite_pk] = {
                'id': str(lite_pk),
                'software': request.POST.get('software'),
                'version': request.POST.get('version')
            }

            return JsonResponse({'Update': f'{version_control[lite_pk]}'})
    except IndexError as error:
        return JsonResponse({'ERROR': f'{error}'})


@csrf_exempt
def delete(request, lite_pk):
    try:
        if request.method == 'POST':
            version_control[lite_pk] = {
                'id': str(lite_pk),
                'software': None,
                'version': None
                }

            return JsonResponse({'Delete': f'{version_control[lite_pk]}'})
    except IndexError as error:
        return JsonResponse({'ERROR': f'{error}'})
