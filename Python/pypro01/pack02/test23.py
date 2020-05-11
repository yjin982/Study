# 우편번호 파일 읽기 : 동 이름 입력 후 해당 자료 출력

try:
    dong = input('동 이름 입력 : ')
    with open('zipcode.txt', 'r', encoding = 'euc-kr') as f:
        line = f.readline() #한 줄씩 읽기
        
        while line: #자료가 있는 동안
            lines = line.split('\t') #\t 혹은 chr(9) 아스키코드9가 탭
            if lines[3].startswith(dong):
                print('[',lines[0],']', lines[1:])
            line = f.readline()
        
except Exception as e:
    print(e)