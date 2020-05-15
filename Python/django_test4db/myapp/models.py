from django.db import models

# Create your models here.
class Article(models.Model):  #테이블 선언
    code = models.CharField(max_length=10)
    sang = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    
