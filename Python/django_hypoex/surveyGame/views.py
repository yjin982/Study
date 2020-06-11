from django.shortcuts import render
from surveyGame.models import SurveyData
import os
from django.contrib import messages
from django.http.response import HttpResponseRedirect

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def GoSurvey(request):
    return render(request, 'gsurvey.html')

def SurveyList(request):
    return render(request, 'list.html')

def SurveyResult(request):
    InsertData(request)
    datas = list(SurveyData.objects.all().values())
    tpv = IndTtest(datas)
    apv = OnewayAnova(datas)
    
    if tpv == 0 or apv == 0:
        return HttpResponseRedirect('error')
    
    return render(request, 'result.html', {'ttest':tpv, 'ftest':apv})

def error(request):
    messages.info(request, '데이터가 충분하지 않아서 분석을 할 수 없습니다.')
    return render(request, 'error.html')


def InsertData(request):
    if request.method == 'POST':
        if request.POST['game_time'] == '':
            print('값이 읎어요')
        else:
            SurveyData(
                job = request.POST['job'],
                gender = request.POST['gender'],
                game_time = request.POST['game_time']
            ).save()
    print('저장 완료')


import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

def IndTtest(datas):
    df = pd.DataFrame(datas)
    #print(df)
    cdir = os.path.dirname(os.path.realpath(__file__))
    
    male_time = df[df['gender'] == '남자']['game_time']
    female_time = df[df['gender'] == '여자']['game_time']
    
    
    #정규성 확인
    try:
        m = stats.shapiro(male_time)[1]
        f = stats.shapiro(female_time)[1]
    except Exception as e:
        print('error ', e)
        return 0
    
    
    # 시각화
    plt.rc('font', family='malgun gothic')            #한글깨짐 방지
    plt.rcParams['axes.unicode_minus'] = False  #마이너스부호 깨짐 방지
    fig1 = plt.figure()
    custom_colors = sns.color_palette(['lightpink', 'lightskyblue'])
    sns.barplot(x="job", y="game_time", hue="gender", data=df, ci=None, palette=custom_colors)
    plt.title('직업과 성별에 따른 게임시간', fontsize=14)
    plt.ylabel('게임 시간', fontsize=14)
    plt.xlabel('직업', fontsize=14)
    fig1 = plt.gcf()
    fig1.savefig('{}\\static\images\\ttest.png'.format(cdir))
    plt.close(fig1)
    
    #등분산성확인 
    lev = stats.levene(male_time, female_time).pvalue
    
    if m > 0.05 and f > 0.05:
        print('정규성 만족')
        if lev > 0.05:
            _, pv = stats.ttest_ind(male_time, female_time, equal_var=True)
            print('등분산성 만족', pv)
        else:
            _, pv = stats.ttest_ind(male_time, female_time, equal_var=False)
            print('등분산성 불만족', pv)
    else:
        _, pv = stats.mannwhitneyu(male_time, female_time)
        print('정규성 불만족', pv)
        
    return pv
    
    
from statsmodels.stats.multicomp import pairwise_tukeyhsd
def OnewayAnova(datas):
    df = pd.DataFrame(datas)
    cdir = os.path.dirname(os.path.realpath(__file__))
    
    job1 = df[df['job'] == '화이트칼라']['game_time']
    job2 = df[df['job'] == '블루칼라']['game_time']
    job3 = df[df['job'] == '학생']['game_time']
    job4 = df[df['job'] == '기타']['game_time']
    
    
    # 정규성 확인
    try:
        j1sp = stats.shapiro(job1)[1]
        j2sp = stats.shapiro(job2)[1]
        j3sp = stats.shapiro(job3)[1]
        j4sp = stats.shapiro(job4)[1]
    except Exception as e:
        print('error ', e)
        return 0
        


    # 시각화
    plt.rc('font', family='malgun gothic')            #한글깨짐 방지
    plt.rcParams['axes.unicode_minus'] = False  #마이너스부호 깨짐 방지
    explode = (0, 0.1, 0, 0)
    fig2 = plt.figure()
    plt.title('직업별 인원 비율', fontsize=14)
    plt.pie(df.groupby('job').size(), labels=df['job'].unique(), colors=["pink", "coral", "lightblue", "yellowgreen"], autopct='%0.1f%%', explode=explode)
    fig2 = plt.gcf()
    fig2.savefig('{}\\static\images\\ftest.png'.format(cdir))
    plt.close(fig2)
    
    
    # 등분산성 확인
    lev = stats.levene(job1, job2, job3, job4).pvalue
    print(lev)
    
    if j1sp > 0.05 and j2sp > 0.05 and j3sp > 0.05 and j4sp > 0.05:
        print('정규성 만족')
        if lev > 0.05:
            _, pv = stats.f_oneway(job1, job2, job3, job4)
            print('등분산성 만족 ', pv)
            
            turk = pairwise_tukeyhsd(df.game_time, df.job)
            print('사후검정\n', turk)
        else:
            _, pv = stats.f_oneway(job1, job2, job3, job4)
            pv = stats.levene(job1, job2, job3, job4, center='trimmed').pvalue
            print('등분산성 불만족')
            
    else:
        _, pv = stats.kruskal(job1, job2, job3, job4)
        print('정규성 불만족  ', pv)
        
    return pv
    