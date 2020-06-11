from django.contrib import admin
from surveyGame.models import SurveyData

# Register your models here.
class SurveyG(admin.ModelAdmin):
    list_display = ('job', 'gender', 'game_time')
    
admin.site.register(SurveyData, SurveyG)