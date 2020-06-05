from django.shortcuts import render
from coffeesurvey.models import Survey

# Create your views here.
def Main(request):
    return render(request, 'main.html')


def SurveyView(request):
    return render(request, 'survey.html')

def SurveyProcess(request):
    InsertData(request)  # 신규 자료 저장
    rdata = list(Survey.objects.all().values())
    result, crosstab, df = ChiFunc(rdata)
    
    return render(request, 'list.html', {'result':result, 'crossTab':crosstab.to_html(), 'df':df.to_html(index=False)})


def InsertData(request):
    if request.method == 'POST':
        Survey(
            # rnum = len(list(Survey.objects.all().values())) + 1, #자동증가 칼럼이 아니면 직접증가
            gender = request.POST['gender'],
            age = request.POST['age'],
            co_survey = request.POST['co_survey'],
        ).save()
    
    
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
def ChiFunc(rdata):
    # print(rdata)
    df = pd.DataFrame(rdata)
    df.dropna()
    df['genNum'] = df['gender'].apply(lambda g:1 if g == '남' else 2) #gender가 남이면 1 아니면 2
    df['coNum'] = df['co_survey'].apply(lambda c:1 if c == '스타벅스' else 2 if c == '투썸플레이스' else 3 if c == '커피빈' else 4)
    #print(df)
    
    # 교차표 작성
    crosstab = pd.crosstab(index=df['genNum'], columns=df['coNum'])
    #print(crosstab)
    
    _, pv, _, _ = stats.chi2_contingency(crosstab)
    print(pv)
    
    if pv >= 0.05:
        result = 'p값이 {} 이므로 0.05 이상의 값을 가지므로 성별에 따라 선호하는 커피 브랜드에는 차이가 없다.(귀무가설 채택)'.format(pv)
    else:
        result = 'p값이 {} 이므로 0.05 미만의 값을 가지므로 성별에 따라 선호하는 커피 브랜드에는 차이가 있다.(귀무가설 기각)'.format(pv)
    
    
    # 시각화 : 커피 브랜드별 선호 건수
    plt.rc('font', family='malgun gothic')            #한글깨짐 방지
    plt.rcParams['axes.unicode_minus'] = False  #마이너스부호 깨짐 방지
    fig = plt.gcf()
    co_group = df['co_survey'].groupby(df['coNum']).count()
    print(co_group)
    
    co_group.plot.bar(subplots=True, color=['pink', 'lightblue', 'sandybrown', 'olivedrab'], width=0.5)
    plt.xlabel('브랜드')
    plt.ylabel('선호 건수')
    plt.title('커피 브랜드별 선호 건수')
    fig.savefig('coffeesurvey/static/images/vbar.png')
    
    
    return result, crosstab, df