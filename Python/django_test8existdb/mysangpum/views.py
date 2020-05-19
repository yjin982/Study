from django.shortcuts import render
from mysangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    #이렇게 해도 되지만 html에서 처리 할 때 리턴타입이 튜플이므로  {{키.0}} 식으로 처리 
    #ORM은 복잡한 쿼리문 실행을 못하기 때문에 그럴 경우에 사용하는 것이 좀더 효율적
    #sql = 'select * from sangdata'
    #conn = Mysql.connect()
    #cursor = conn.cursor()
    #cursor.execute(sql)
    #datas = cursor.fetchall() 
    ''' 
    페이징 처리 안 된 일반적인 상태
    datas = Sangdata.objects.all()   #ORM일 경우 리턴타입이 QuerySet -> {{키.컬럼명}}
    return render(request, 'list.html', {'sangpums':datas})
    '''
    '''페이지 나누기 기능은 list2.html에서 출력'''
    datas = Sangdata.objects.all().order_by('-code') #code desc
    paginater = Paginator(datas, 5)   #페이지당 5개씩 보기
    
    try:
        page = request.GET['page']
    except:
        page = 1
        
    try:
        data = paginater.page(page)
    except PageNotAnInteger:
        data = paginater.page(1)     #페이지 변수가 숫자가 아닌 경우 1페이지로
    except EmptyPage:
        data = paginater.page(paginater.num_pages())   #페이지가 없는 경우
        
    #개별 페이지 표시용 작업
    allpage = range(paginater.num_pages + 1)
    #print(allPage)
    
    return render(request, 'list2.html', {'sangpums':data, 'allpage':allpage})
    
def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        #print(request.POST['sang'])
        Sangdata(
            code = request.POST['code'],
            sang = request.POST['sang'],
            su = request.POST['su'],
            dan = request.POST['dan']
        ).save()
        
    return HttpResponseRedirect('/sangpum/list') #추가 후 목록보기(리다이렉트)

def UpdateFunc(request):
    data = Sangdata.objects.get(code=request.GET['code'])
    return render(request, 'update.html', {'sang_one':data})

def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST['code'])
        upRec.code = request.POST['code']
        upRec.sang = request.POST['sang']
        upRec.su = request.POST['su']
        upRec.dan = request.POST['dan']
        upRec.save() #수정 완료
    return HttpResponseRedirect('/sangpum/list') #수정 후 목록보기
    

def DeleteFunc(request):
    delRec = Sangdata.objects.get(code=request.GET['code'])
    delRec.delete()
    return HttpResponseRedirect('/sangpum/list') #삭제 후 목록보기
    