from django.shortcuts import render
from mysangpum.models import Sangdata
from django.http.response import HttpResponse
import json

# Create your views here.
def Main(request):
    return render(request, 'main.html')


def List(request):
    return render(request, 'list.html')


def Show(request):
    sdata = Sangdata.objects.all()
    datas = []
    
    for s in sdata:
        dicData = {'code':s.code, 'sang':s.sang, 'su':s.su, 'dan':s.dan}
        datas.append(dicData) #리스트 안에 dict 데이터가 들어간 형태
        
    return HttpResponse(json.dumps(datas), content_type='application/json')