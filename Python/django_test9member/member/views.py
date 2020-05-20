from django.shortcuts import render
from member.models import MemTable
import MySQLdb
from django.http.response import HttpResponseRedirect
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'dbmember',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

# Create your views here.
def Main(request):
    return render(request, 'main.html')


def ListFunc(request):
    datas = MemTable.objects.all()
    return render(request, 'list.html', {'members':datas})


def IdCheckFunc(request):
    memid = request.GET['memid']
    isRegister = False #해당 id의 회원 등록 여부 판단
    
    try:#id가 없으면 except
        '''방법1 ORM 사용
        data = MemTable.objects.get(memid=memid)
        if data:
            isRegister = True
        '''
        
        '''방법2 SQL문 기술'''
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select * from member_memtable where memid='{}'".format(memid)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data != None: #data가 없으면 None
            isRegister = True
        
    except Exception as e:
        print('IdCheckFunc Error ->', e)
    finally:
        cursor.close()
        conn.close()
        
    return render(request, 'idcheck.html', {'memid':memid, 'isReg':isRegister})


def ZipCheckFunc(request):
    chk = request.GET['check']    
    return render(request, 'zipcheck.html', {'check':chk})

def ZipCheckOkFunc(request): #우편번호 찾기 작업
    area3 = request.POST['area3']
    
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select * from member_ziptab where area3 like '{}%'".format(area3)
        cursor.execute(sql)
        datas = cursor.fetchall()
        #print(datas) #튜플타입
    except Exception as e:
        pass
    finally:
        cursor.close()
        conn.close()
        
    return render(request, 'zipcheck.html', {'addrs':datas, 'check':'n'})


def InsertFunc(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    elif request.method == 'POST':
        MemTable(
            memid = request.POST['memid'],
            passwd = request.POST['passwd'],
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            zipcode = request.POST['zipcode'],
            address = request.POST['address'],
            job = request.POST['job'],
        ).save()
        return HttpResponseRedirect('/member/list') #등록 후 회원목록 보기
    else:
        return render(request, 'error.html')

