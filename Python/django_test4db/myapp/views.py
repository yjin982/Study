from django.shortcuts import render
from myapp.models import Article

# Create your views here.
def main(request):
    return render(request, 'main.html')

def dbtest(request):
    datas = Article.objects.all()   #장고의 ORM, select * from Article  (내부적으로는 myapp_article)
    #print(datas)   #<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
    #print(datas[i].sang)
    return render(request, 'articlelist.html', {'articles':datas})