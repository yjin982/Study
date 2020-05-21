from django.shortcuts import render
from myboard.models import BoardTab
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponseRedirect
from datetime import datetime

# Create your views here.
def Main(request):
    aa = "<div><h1>views에서 만든 태그</h1></div>"
    return render(request, 'main.html', {'msg':aa})

def ListFunc(request):  #게시판 목록 보기
    #datas = BoardTab.objects.all().order_by('-id')  #id를 기준으로 desc
    datas = BoardTab.objects.all().order_by('-gnum', 'onum')
    paginator = Paginator(datas, 5)   #한 페이지당 5행 출력
    page = request.GET.get('page')   #GET['page'] 했을땐 안됐는데 왠지 모름 
    
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
        
    return render(request, 'board.html', {'data':data})


def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request): #추가
    if request.method == 'POST':
        try:
            gbun = 1
            datas = BoardTab.objects.all()   #group 번호 구하기
            if datas.count() != 0: #자료가 있는 경우
                gbun = BoardTab.objects.latest('id').id + 1
            
            BoardTab(
                name = request.POST['name'],
                passwd = request.POST['passwd'],
                mail = request.POST['mail'],
                title = request.POST['title'],
                cont = request.POST['cont'],
                bip = request.META['REMOTE_ADDR'], #아이피 구하기
                bdate = datetime.now(),   #현재 날짜
                readcnt = 0,   #조회수
                gnum = gbun,
                onum = 0,
                nested = 0,
            ).save() #추가
            
        except Exception as e:
            print('InsertOkFunc error ', e)
            
    return HttpResponseRedirect('/board/list')   #추가 후 목록보기

def SearchFunc(request):   #검색
    if request.method == 'POST':
        s_type = request.POST['s_type']   #검색 유형 : 작성자 혹은 제목으로 검색
        s_value = request.POST['s_value']#검색내용
        
        if s_type == 'title':
            datas = BoardTab.objects.filter(title__contains = s_value).order_by('-id') #칼럼명__contains는 like연산자 처럼 작업됨
        elif s_type == 'name':
            datas = BoardTab.objects.filter(name__contains = s_value).order_by('-id')
        
        #페이징처리
        paginator = Paginator(datas, 5)
        page = request.GET.get('page')
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
            
    return render(request, 'board.html', {'data':data})
    
    
def ContentFunc(request): #글 내용보기
    data = BoardTab.objects.get(id=request.GET['id'])
    data.readcnt = data.readcnt + 1 #조회수 증가
    data.save()
    
    page = request.GET['page']
    return render(request, 'content.html', {'data_one':data, 'page':page})
    
    
def UpdateFunc(request):
    try:
        data = BoardTab.objects.get(id=request.GET['id'])
    except Exception as e:
        print('UpdateFunc error ', e)
    return render(request, 'update.html', {'data_one':data})

def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = BoardTab.objects.get(id=request.POST['id'])
        if upRec.passwd == request.POST['up_passwd']: #게시글 비밀번호 비교
            upRec.name = request.POST['name']
            upRec.mail = request.POST['mail']
            upRec.title = request.POST['title']
            upRec.cont = request.POST['cont']
            upRec.save() #수정 반영
        else:
            return render(request, 'error.html')
    return HttpResponseRedirect('/board/list') #수정 후 목록보기

def DeleteFunc(request):
    try:
        data = BoardTab.objects.get(id=request.GET['id'])
    except Exception as e:
        print('DeleteFunc error', e)
    return render(request, 'deleteok.html', {'data':data})

def DeleteOkFunc(request):
    if request.method == 'POST':
        delRec = BoardTab.objects.get(id=request.POST['id'])
        if delRec.passwd == request.POST['del_passwd']:
            delRec.delete()
            return HttpResponseRedirect('/board/list')
        else:
            return render(request, 'error.html')

def ReplyFunc(request):
    try:
        redata = BoardTab.objects.get(id=request.GET['id'])
        
    except Exception as e:
        print('ReplyFunc error ', e)
    return render(request, 'reply.html', {'data_one':redata})

def ReplyOkFunc(request):
    if request.method == 'POST':
        try:
            regnum = int(request.POST['gnum']) #String으로 넘어오기때문에 int형변환
            reonum = int(request.POST['onum'])
            
            tempRec = BoardTab.objects.get(id=request.POST['id'])
            old_gnum = tempRec.gnum
            old_onum = tempRec.onum
            
            if old_gnum >= reonum and old_gnum == regnum:
                old_onum += 1  #onum 갱신
            
            #답글 저장
            BoardTab(
                name = request.POST['name'],
                passwd = request.POST['passwd'],
                mail = request.POST['mail'],
                title = request.POST['title'],
                cont = request.POST['cont'],
                bip = request.META['REMOTE_ADDR'], #아이피 구하기
                bdate = datetime.now(),   #현재 날짜
                readcnt = 0,   #조회수
                gnum = regnum,
                onum = old_onum,
                nested = int(request.POST['nested']) +1,                 
            ).save()
            return HttpResponseRedirect('/board/list') #답글 작성 후 목록보기

        except Exception as e:
            print('ReplyOkFunc error ', e)
            return render(request, 'error.html')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    