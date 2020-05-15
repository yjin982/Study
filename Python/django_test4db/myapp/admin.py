from django.contrib import admin
from myapp.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'sang', 'price', 'pub_date') #어드민페이지에서 테이블 칼럼명과 데이터가 테이블형식으로 보이게 

admin.site.register(Article, ArticleAdmin) #어드민페이지에서 테이블을 등록