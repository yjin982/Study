from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('인덱스 요청 처리')

def helloFunc(request):
    msg = '장고 쟝고'
    temp = "<html><body>장고 수행 메세지: {0}</body></html>".format(msg)
    return HttpResponse(temp)

def helloTemFunc(request):
    mymsg = '홍길동'
    return render(request, 'show.html', {'msg':mymsg})

def worldFunc(request):
    return render(request, 'disp.html')