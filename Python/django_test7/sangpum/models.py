from django.db import models

# Create your models here.
class Maker(models.Model):
    mname = models.CharField(max_length=10)
    tel = models.CharField(max_length=20)
    addr = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('-id', )
    
    def __str__(self):       #관리자페이지와 관련
        return self.mname   #id대신 id에 해당하는 mname이 보이도록? 해줌
    

class Product(models.Model):
    pname = models.CharField(max_length=10)
    price = models.IntegerField()
    maker_name = models.ForeignKey(Maker, on_delete=models.CASCADE) 
    '''
    실제 db에서는  maker_name은 maker_name_id로 생성
    CASCADE, 외래키가 참조하는 데이터를 삭제시 같이 삭제되는 옵션(=메이커의 버거킹을 삭제시 그에 연결된 데이터 전체), 실제는 프로그래밍으로 처리하는 편이 더 좋음
    '''