from django.db import models

# Create your models here.
class SurveyData(models.Model):
    GENDER_CHOICE = (
        ('남자', '남자'),
        ('여자', '여자')
    )
    JOB_CHOICE = (
        ('화이트칼라', '화이트칼라'),
        ('블루칼라', '블루칼라'),
        ('학생', '학생'),
        ('기타', '기타')
    )
    job = models.CharField(max_length=10, choices=JOB_CHOICE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    game_time = models.FloatField()
    
    class Meta:
        ordering = ('-id', )
