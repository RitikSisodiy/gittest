from django.shortcuts import render
from .models import postdata
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
@csrf_exempt
def pull(request):
    if request.method == 'POST':
        res ={}
        for data in request.POST:
            res[data] = request.POST[data]
            os.system('git checkout .')
            os.system('git pull')
            os.system('touch tmp/restart.txt')
            postdata(data=str(res),host=request.get_host()).save()
    return HttpResponse('successvv')
def home(request):
    return HttpResponse("it worked with host")