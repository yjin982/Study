from django.shortcuts import render, get_object_or_404
from myvote.models import Question, Choise
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')


def DispFunc(request):
    q_list = Question.objects.all().order_by('pub_date', 'id')
    context = {'q_list':q_list}
    return render(request, 'display.html', context)

def DetailFunc(request, question_id):  # /govote/1
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not Exist")
    question = get_object_or_404(Question, pk=question_id)
    
    #print(question, '==', question.question_text)
    return render(request, 'detail.html', {'question':question})

def VoteFunc(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        sel_choice = question.choise_set.get(pk=request.POST['choice'])
    except (KeyError, Choise.DoesNotExist):
        return render(request, 'detail.html', {'question':question, 'error_msg':'투표 항목을 선택하시오'})
    
    sel_choice.votes += 1
    sel_choice.save() #투표 항목을 1 누적 후 갱신
    return HttpResponseRedirect(reverse('results', args=(question.id, ))) #<int:question_id>/results/ 요청을 매핑


def ResultFunc(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question':question})