#레이아웃 매니저 중 BoxSizer()
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 400))
        
        panel1 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        panel2 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        
        panel1.SetBackgroundColour('blue')
        panel2.SetBackgroundColour('red')
        
        box = wx.BoxSizer(wx.VERTICAL) #HORIZONTAL, VERTICAL옵션
        box.Add(panel1, 1, wx.EXPAND)  # 1/3 영역 확보
        box.Add(panel2, 2, wx.EXPAND)  # 2/3 영역 확보
        self.SetSizer(box)
        
        self.Center()
        self.Show()
        
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title='BoxSizer 연습')
    app.MainLoop() #무한루프