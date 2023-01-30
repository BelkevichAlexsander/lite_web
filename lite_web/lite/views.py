from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


version_control = []


@csrf_exempt
def version(request):
    if request.method == 'GET':
        if not version_control:
            return HttpResponse('ERROR: Dictionary version is empty')

        return HttpResponse(version_control)

    elif request.method == 'POST':
        version_control.append({
            'id': str(len(version_control)),
            'software': request.POST.get('software'),
            'version': request.POST.get('version')
        })
        print(version_control)

        return HttpResponse(f'Create: {version_control[len(version_control) - 1]}')
    else:
        return HttpResponse('ERROR: This method POST is not correct')


def one_version(request, lite_pk):
    if request.method == 'GET':
        return HttpResponse(f'Selected version: {version_control[lite_pk]}')
    else:
        return HttpResponse('ERROR: This version is not created. Please create!')


@csrf_exempt
def correct(request, lite_pk):
    if request.method == 'POST':
        version_control[lite_pk] = {
            'id': str(lite_pk),
            'software': request.POST.get('software'),
            'version': request.POST.get('version')
        }

        return HttpResponse(f'Update: {version_control[lite_pk]}')
    else:
        return HttpResponse('ERROR: This is not POST method for correct')


@csrf_exempt
def delete(request, lite_pk):
    if request.method == 'POST':
        version_control[lite_pk] = {
            'id': str(lite_pk),
            'software': 'delete software',
            'version': 'delete version'
            }

        return HttpResponse(f'Delete: {version_control[lite_pk]}')
    else:
        return HttpResponse('ERROR: This is not POST method for delete')
