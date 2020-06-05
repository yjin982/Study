from django.urls import path
from coffeesurvey import views

urlpatterns = [
    path('survey/', views.SurveyView),
    path('surveyprocess', views.SurveyProcess),
]
