#GUI 프로그래밍 - wxPython 라이브러리
import wx
''' 확인하기
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)  
app.MainLoop()
'''
class Ex(wx.Frame):
    def __init__(self, parent, title):
        super(Ex, self).__init__(parent, title=title, size=(400, 400)) #상속받은 Frame 생성자
        
        self.CreateStatusBar()     #상태표시줄
        
        #Menu 추가
        menubar = wx.MenuBar()
        mnuFile = wx.Menu()
        mnuNew = mnuFile.Append(wx.ID_NEW, 'New', '새글')
        mnuOpen = mnuFile.Append(wx.ID_OPEN, 'Open', '열기')
        mnuFile.AppendSeparator() #구분선
        mnuExit = mnuFile.Append(wx.ID_EXIT, 'Exit', '종료')
        menubar.Append(mnuFile, 'File')
        self.SetMenuBar(menubar)
        
        #라벨과 텍스트박스 생성
        panel = wx.Panel(self)
        wx.StaticText(panel, label='i   d : ', pos=(5, 5))   #pos = (x, y) 창 내에서의 좌표
        wx.StaticText(panel, label='pwd : ', pos=(5, 40)) #라벨은 지적할 필요가 없으니까 이름을 주지 않음
        self.txtA = wx.TextCtrl(panel, pos=(40, 5))   #기본 싱글라인이기 때문에 멀티라인을 주고 싶으면 style=wx.TE_MULTILINE)
        self.txtB = wx.TextCtrl(panel, pos=(40, 40)) #text박스 사이즈는 size=(x,y) 로 y에 -1을 주면 알아서 
        
        #버튼
        btn1 = wx.Button(panel, label='일반버튼', pos=(5, 80))
        btn2 = wx.ToggleButton(panel, label='토글버튼', pos=(90, 80))
        btn3 = wx.Button(panel, label='종료', pos=(175, 80), size=(50, -1))
        
        #메뉴에 이벤트 장착
        self.Bind(wx.EVT_MENU, self.OnEvent1, mnuNew)
        self.Bind(wx.EVT_MENU, self.OnEvent2, mnuExit)
        
        #이벤트 처리 방법 1 : 각 각 버튼에 이벤트
        #btn1.Bind(wx.EVT_BUTTON, self.OnClick1)
        #btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClick2)
        #btn3.Bind(wx.EVT_BUTTON, self.OnClick3)
        
        #이벤트 처리 방법 2(하나의 이벤트 핸들러 호출) - id 사용
        btn1.id = 1
        btn2.id = 2
        btn3.id = 3
        btn1.Bind(wx.EVT_BUTTON, self.OnClickAbc)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClickAbc)
        btn3.Bind(wx.EVT_BUTTON, self.OnClickAbc)
        
        self.Center()
        self.Show()
        
    
    def OnEvent1(self, event):#OnEvent1() takes 1 positional argument but 2 were given : 이벤트는 이벤트처리할 인자를 하나 더 줘야함
        self.txtA.SetLabelText('새글 메뉴 누름')
        
    def OnEvent2(self, event):
        self.Close(True)
    
    def OnClick1(self, event):
        #대화상자 호출
        msgDial = wx.MessageDialog(self, '메세지', '제목', wx.OK)
        msgDial.ShowModal()
        msgDial.Destroy()
        
        self.SetTitle('버튼 1 클릭')
    
    def OnClick2(self, event):
        #print(event.GetEventObject().GetValue()) #토글버튼 value 보기
        if event.GetEventObject().GetValue(): #true 일때
            self.txtA.SetLabelText('good')
            self.txtB.SetLabelText('text')
        else:
            self.txtA.SetLabelText('')
            self.txtB.SetLabelText('')
    
    def OnClick3(self, event):
        self.Close()
    
    def OnClickAbc(self, event): #버튼 동적 처리 가능
        bid = event.GetEventObject().id
        
        if bid == 1:
            self.SetTitle('btn1')
        elif bid == 2:
            self.SetTitle('btn2')
        else:
            self.Close()
    
    
if __name__ == '__main__':
    app = wx.App()
    Ex(None, title='연습')
    app.MainLoop() #무한루프