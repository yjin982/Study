from django.urls import path
from surveyGame import views


urlpatterns = [
    path('', views.SurveyList),
    path('gosurvey', views.GoSurvey),
    path('list', views.SurveyList),
    path('result', views.SurveyResult),
    path('error', views.error),
]
