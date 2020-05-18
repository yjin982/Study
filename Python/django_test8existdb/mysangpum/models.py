from django.db import models

# Create your models here.
'''
    프롬프트에서 python manage.py inspectdb > sang.py 로 인해서 생긴 파일에서 가져옴
    이미 있는 DB에서 테이블을 가져온 것
'''
class Sangdata(models.Model):
    code = models.IntegerField(primary_key=True) #기본키를 걸었기 때문에 id 자동생성 X
    sang = models.CharField(max_length=20, blank=True, null=True)
    su = models.IntegerField(blank=True, null=True)
    dan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangdata'