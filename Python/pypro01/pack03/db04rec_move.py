import wx
import wx.xrc
import ast
import MySQLdb

rec_r = 0
datas = []
with open('mariadb.txt', 'r') as con:
    config = ast.literal_eval(con.read())
    
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetBackgroundColour( wx.Colour( 232, 242, 255 ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"코드 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtCode = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtCode.SetEditable(False)
        bSizer2.Add( self.txtCode, 1, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"품명 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txtSang = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtSang.SetEditable(False)
        bSizer2.Add( self.txtSang, 1, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"수량 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txtSu = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtSu.SetEditable(False)
        bSizer3.Add( self.txtSu, 1, wx.ALL, 5 )
        
        self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"단가 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.txtDan = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtDan.SetEditable(False)
        bSizer3.Add( self.txtDan, 1, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"금액 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.staKum = wx.StaticText( self.m_panel3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staKum.Wrap( -1 )
        bSizer4.Add( self.staKum, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel4, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn1, 1, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel4, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn2, 1, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel4, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn3, 1, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel4, wx.ID_ANY, u">>||", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn4, 1, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn1.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn2.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn3.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn4.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn1.id = 1
        self.btn2.id = 2
        self.btn3.id = 3
        self.btn4.id = 4
        
        self.DbLoad()
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def onClick( self, event ):
        id = event.GetEventObject().id
        global rec_r
        
        if id == 1:   #처음
            rec_r = 0
        elif id == 2:#이전
            rec_r -= 1
            if rec_r < 0: rec_r = 0
        elif id == 3:#다음
            rec_r += 1
            if rec_r > (len(datas) - 1): rec_r = len(datas) - 1
        elif id == 4:#끝
            rec_r = len(datas) - 1
        else:
            pass
        
        self.ShowData(rec_r)
        
        
    def DbLoad(self):
        try:
            conn = MySQLdb.connect(**config);
            cursor = conn.cursor()
            
            global datas
            sql = "select * from sangdata"
            cursor.execute(sql)
            datas = cursor.fetchall()
            self.ShowData(rec_r)
            
        except Exception as e:
            print('DbLoad error ', e)
            
        finally:
            cursor.close()
            conn.close()
    
    def ShowData(self, r):
        self.txtCode.SetLabelText(str(datas[r][0]))
        self.txtSang.SetLabelText(datas[r][1])
        self.txtSu.SetLabelText(str(datas[r][2]))
        self.txtDan.SetLabelText(str(datas[r][3]))
        self.staKum.SetLabelText(str(datas[r][2] * datas[r][3]))
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop() 