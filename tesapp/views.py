from django.shortcuts import render
from .models import postdata
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def pull(request):
    if request.method == 'POST':
        res ={}
        for data in request.POST:
            res[data] = request.POST[data]
            postdata(data=str(res)).save()
    return HttpResponse('successvv')