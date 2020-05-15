from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def MainFunc(request):
    return render(request, 'index.html')


class CallView(TemplateView):
    template_name = 'callget.html'


def InsertFunc(request):
    if request.method == 'GET':
        print('get 요청 처리')
        return render(request, 'insert.html')
    elif request.method == 'POST':
        print('post 요청 처리')
        irum1 = request.POST['name']
        irum2 = request.POST.get('name')
        
        return render(request, 'list.html', {'irum':irum1})
    else:
        print('요청 오류')