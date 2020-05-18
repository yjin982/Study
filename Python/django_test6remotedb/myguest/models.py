from django.db import models
from hypothesis.internal.conjecture.shrinking import ordering

# Create your models here.
class Guest(models.Model): #database가 비워져있어도 이대로 테이블이 생성됨
    title = models.CharField(max_length=50)
    content = models.TextField()
    regdate = models.DateTimeField()
    #app이름_클래스이름 으로 db에서 테이블이 생성됨
    
    class Meta:              #정렬 방법 2: model의 클래스를 이용
        ordering = ('-id',)  #반드시 튜플이어야 함
        #ordering = ('title', '-id')   #제목별로 asc하고 동일한경우 id로 desc한다는 것
