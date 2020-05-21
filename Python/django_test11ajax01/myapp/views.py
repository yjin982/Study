import json
from django.shortcuts import render
from django.http.response import  HttpResponse


# Create your views here.
def Main(request):
    #jsonTest()    
    return render(request, 'main.html')

def Func1(request):
    msg = request.GET['msg']
    print(msg, type(msg))
    context = {'key':msg}          #str
    
    print(context, type(context)) #dict
    print(json.dumps(context), type(json.dumps(context)))
    
    return HttpResponse(json.dumps(context), content_type='application/json')






lan = {
    'id':111,
    'name':'메머드',
    'history':[
        {'date':'2020-5-21', 'exam':'사냥의 정석'},
        {'date':'2020-5-11', 'exam':'가죽공방'},
    ]
}
def jsonTest():
    print(type(lan)) #dict type
    
    '''JSON 인코딩'''
    jsonString = json.dumps(lan)
    print(jsonString)   #type은 str  
    #{"id": 111, "name": "\uba54\uba38\ub4dc", "history": [{"date": "2020-5-21", "exam": "\uc0ac\ub0e5\uc758 \uc815\uc11d"}, {"date": "2020-5-11", "exam": "\uac00\uc8fd\uacf5\ubc29"}]}
    
    jsonString = json.dumps(lan, indent=4)
    print(jsonString)   #indent(들여쓰기) 넣은 경우  
    '''
    {
        "id": 111,
        "name": "\uba54\uba38\ub4dc",
        "history": [
            {
                "date": "2020-5-21",
                "exam": "\uc0ac\ub0e5\uc758 \uc815\uc11d"
            },
            {
                "date": "2020-5-11",
                "exam": "\uac00\uc8fd\uacf5\ubc29"
            }
        ]
    }
    '''
    
    '''JSON 디코딩   str => python object'''
    dic = json.loads(jsonString)
    print(dic, type(dic))
    #{'id': 111, 'name': '메머드', 'history': [{'date': '2020-5-21', 'exam': '사냥의 정석'}, {'date': '2020-5-11', 'exam': '가 죽공방'}]} <class 'dict'>
    
    print(dic['history'][0]['exam']) #사냥의 정석
    for h in dic['history']:
        print(h['date'], ' ', h['exam'])