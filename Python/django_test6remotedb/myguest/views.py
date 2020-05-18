from django.shortcuts import render
from myguest.models import Guest
from django.http.response import HttpResponseRedirect
from datetime import datetime

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    gdata = Guest.objects.all()                               #ORM, 기본 : id별 asc
    #data = Guest.objects.all().order_by('-id')          #정렬방법1 : order_by 메소드, desc 컬럼명 앞에 - 
    #gdata = Guest.objects.all().order_by('-id')[0:2] #갯수 제한
    
    return render(request, 'list.html', {'gdata':gdata})  #forward

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        #print(request.POST.get('title'))
        #print(request.POST['title'])
        Guest(
            title = request.POST['title'],
            content = request.POST['content'],
            regdate = datetime.now()
        ).save() #ORM의 추가
        return HttpResponseRedirect('/guest')   #추가 후 목록 보기
    else:
        return HttpResponseRedirect('/guest/insert')