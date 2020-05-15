from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def main(request):
    return render(request, 'main.html')  #포워딩

def setos(request):
    if 'favorite_os' in request.GET:
        print(request.GET['favorite_os'])
        request.session['f_os'] = request.GET['favorite_os']
        return HttpResponseRedirect('/showos')   #리다이렉팅, showos 요청이 발생
    else:
        return render(request, 'setos.html')
    
def showos(request):
    context = {} #dict
    
    if 'f_os' in request.session: #세션 키 중에서 'f_os'가 있다면
        context['f_os'] = request.session['f_os'] #request.session.get('f_os')
        context['message'] = '당신이 선택한 운영체제는 %s'%request.session['f_os']
        print(context)
    else:
        context['f_os'] = None
        context['message'] = 'fail to choice os'
    
    request.session.set_expiry(5)  #5초간 세션 유효
    return render(request, 'show.html', context)