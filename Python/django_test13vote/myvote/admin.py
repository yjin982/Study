from django.contrib import admin
from myvote.models import Question, Choise

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')
    
class ChoiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'votes')
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choise, ChoiseAdmin)