from django.shortcuts import render


dct_version = []


def index(request):
    return render(request, 'lite/index.html')


def version(request):
    if request.method == 'GET':
        return render(request, 'lite/version.html')
    else:
        if request.POST['software'] is not None or request.POST['version'] is not None:

            dct_version.append({
                'id': len(dct_version),
                'software': request.POST.get('software'),
                'version': request.POST.get('version')
            })

            return render(
                request, 'lite/index.html', {'error': 'object save'}
            )
        else:
            return render(
                request, 'lite/index.html', {"error": "object don't save"}
            )


def versions(request):
    return render(request, 'lite/versions.html', {"lst": dct_version})


def openid(request, lite_pk):
    if request.method == 'GET':
        for x in dct_version:
            if x['id'] == lite_pk:
                return render(request, 'lite/id.html', {'item': x})


def correct(request, lite_pk):
    if request.method == 'POST':
        print('correct')
        for i, x in enumerate(dct_version):
            if x['id'] == lite_pk:
                dct_version[i] = {
                    'id': lite_pk,
                    'software': request.POST.get('software'),
                    'version': request.POST.get('version')
                }

                return render(request, 'lite/index.html', {'error': {f'id: {lite_pk} is correct'}})
    else:
        return render(request, 'lite/index.html', {'error': {'mistake correct'}})


def delete(request, lite_pk):
    if request.method == 'POST':
        print('delete')
        for i, x in enumerate(dct_version):
            if x['id'] == lite_pk:
                dct_version[i] = {
                    'id': lite_pk,
                    'software': 'delete software',
                    'version': 'delete version'
                }
                return render(request, 'lite/index.html', {'error': {f'id: {lite_pk} is delete. This id is null'}})
    else:
        return render(request, 'lite/index.html', {'error': {'mistake delete'}})
