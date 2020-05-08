#클래스의 포함관계로 로또 번호 출력
import random

class LottoBall:
    def __init__(self, num):
        self.num = num
    

class LottoMachine:
    def __init__(self):
        self.ballList = []
        for i in range(1, 46):
            self.ballList.append(LottoBall(i))
    
    def selectBalls(self):
        #공을 섞기 전
        '''
        for i in range(45):
            print(self.ballList[i].num, end = ' ')
        '''
        random.shuffle(self.ballList)

        #공을 섞은 후
        '''
        for i in range(45):
            print(self.ballList[i].num, end = ' ')
        '''
        return self.ballList[0:5]


class LottoUser:
    def __init__(self):
        self.machine = LottoMachine() #포함
    
    def playLotto(self):
        input('로또를 시작합니다. 아무키나 누르세요')
        selectedBalls = self.machine.selectBalls()
        for ball in selectedBalls:
            print('%d'%(ball.num), end=' ')


if __name__ == '__main__': # 시험에 낼거같은 느낌적인 느낌
    LottoUser().playLotto()