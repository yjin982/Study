'''
    미일중 관광객의 한국 관광지 선호 지역 상관관계 분석
'''
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rc('font', family='malgun gothic')            #한글깨짐 방지
plt.rcParams['axes.unicode_minus'] = False  #마이너스부호 깨짐 방지

def setScatterAndCorr(tour_table, all_table, tourpoint): #'창덕궁' '운현궁' '경복궁' '창경궁' '종묘' 순서대로 처리
    # 계산할 관광지명에 해당하는 데이터(날짜)만 뽑아 tour에 저장하고, 외국인 관광객 자료와 병합.
    tour = tour_table[tour_table['resNm'] == tourpoint]
    merge_table = pd.merge(tour, all_table, left_index=True, right_index=True)
    # print(merge_table)
    
    plt.subplot(1, 3, 1)
    plt.xlabel('중국인 입장수')
    plt.ylabel('외국인 입장객수')
    #상관계수 r 얻기
    lamb1 = lambda p:merge_table['china'].corr(merge_table['ForNum'])
    r1 = lamb1(merge_table)
    plt.title('{}\n상관계수 r{:.5f}'.format(tourpoint, r1)) # 상관계수를 그래프 제목에 표시
    plt.scatter(merge_table['china'], merge_table['ForNum'], s=6, c='red', alpha=0.4)
    
    
    plt.subplot(1, 3, 2)
    plt.xlabel('일본인 입장수')
    #상관계수 r 얻기
    lamb2 = lambda p:merge_table['japan'].corr(merge_table['ForNum'])
    r2 = lamb2(merge_table)
    plt.title('{}\n상관계수 r{:.5f}'.format(tourpoint, r2)) # 상관계수를 그래프 제목에 표시
    plt.scatter(merge_table['japan'], merge_table['ForNum'], s=6, c='green', alpha=0.4)
    
      
    plt.subplot(1, 3, 3)
    plt.xlabel('미국인 입장수')
    #상관계수 r 얻기
    lamb3 = lambda p:merge_table['usa'].corr(merge_table['ForNum'])
    r3 = lamb3(merge_table)
    plt.title('{}\n상관계수 r{:.5f}'.format(tourpoint, r3)) # 상관계수를 그래프 제목에 표시
    plt.scatter(merge_table['usa'], merge_table['ForNum'], s=6, c='blue', alpha=0.4)
    
    plt.tight_layout() # 그래프간 여백주기
    plt.show()
    
    return tourpoint, r1, r2, r3
    
    
    
def ready():
    fname = '../testdata/서울특별시_관광지입장정보_2011_2016.json'
    jsonTP = json.loads(open(fname, 'r', encoding='utf8').read())
    # print(jsonTP)
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm', 'resNm', 'ForNum')) # 년월, 관광지명, 외국인 입장객수
    tour_table = tour_table.set_index('yyyymm')
    print(tour_table.head())
    
    # 관광지 이름 얻기
    resNm = tour_table.resNm.unique()
    print('대상 관광지명 :', resNm[:5])
    
    # 중국인 관광객 정보
    cdata = json.loads(open('../testdata/중국인방문객.json', 'r', encoding='utf8').read())
    china_table = pd.DataFrame(cdata, columns=('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns = {'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    # print(china_table.head())

    # 일본인 관광객 정보
    jdata = json.loads(open('../testdata/일본인방문객.json', 'r', encoding='utf8').read())
    japan_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns = {'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    # print(japan_table.head())
    
    # 미국인인 관광객 정보
    adata = json.loads(open('../testdata/미국인방문객.json', 'r', encoding='utf8').read())
    usa_table = pd.DataFrame(adata, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns = {'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    # print(usa_table.head())
    
    # merge
    all_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    all_table = pd.merge(all_table, usa_table, left_index=True, right_index=True)
    print(all_table.head())
    
    
    r_list = [] # 각 관광지(5군데) 마다 상관계수를 구해서 저장
    for tourpoint in resNm[:5]:
        # 시각화 + 상관계수 처리 함수를 호출
        r_list.append(setScatterAndCorr(tour_table, all_table, tourpoint))
    
    print()
    print()
    
    r_df = pd.DataFrame(r_list, columns=('관광지명', '중국', '일본', '미국'))
    r_df = r_df.set_index('관광지명')
    print(r_df)
    
    r_df.plot(kind='bar', rot=50)
    plt.show()

    
if __name__ == '__main__':
    ready()

