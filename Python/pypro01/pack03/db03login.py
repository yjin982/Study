# GUI
import wx
import wx.xrc
import MySQLdb
import sys

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"직원 관리 고객", pos = wx.DefaultPosition, size = wx.Size( 604,477 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetBackgroundColour( wx.Colour( 232, 242, 255 ) )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"사번 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.txtNo = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtNo, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"직원명 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.btnLogin = wx.Button( self.m_panel1, wx.ID_ANY, u"로그인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btnLogin, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel1.SetSizer( bSizer4 )
        self.m_panel1.Layout()
        bSizer4.Fit( self.m_panel1 )
        bSizer3.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.staMsg = wx.StaticText( self.m_panel2, wx.ID_ANY, u"정보", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staMsg.Wrap( -1 )
        bSizer5.Add( self.staMsg, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer5 )
        self.m_panel2.Layout()
        bSizer5.Fit( self.m_panel2 )
        bSizer3.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstGogek = wx.ListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer6.Add( self.lstGogek, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel3.SetSizer( bSizer6 )
        self.m_panel3.Layout()
        bSizer6.Fit( self.m_panel3 )
        bSizer3.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staCount = wx.StaticText( self.m_panel4, wx.ID_ANY, u"인원수 : 0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer7.Add( self.staCount, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel4.SetSizer( bSizer7 )
        self.m_panel4.Layout()
        bSizer7.Fit( self.m_panel4 )
        bSizer3.Add( self.m_panel4, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer3 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        #lstGogek 객체에 제목
        self.lstGogek.InsertColumn(0, '고객번호', width=60)
        self.lstGogek.InsertColumn(1, '고객명', width=100)
        self.lstGogek.InsertColumn(2, '고객전화', width=200)
        
        
        # Connect Events
        self.btnLogin.Bind( wx.EVT_BUTTON, self.onLogin )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def onLogin( self, event ): #로그인 입력값 검사
        if self.txtNo.GetValue() == '':
            wx.MessageBox('사번을 입력하세요', '알림', wx.OK)
            self.txtNo.SetFocus()
            return
        
        if self.txtName.GetValue() == '':
            wx.MessageBox('이름을 입력하세요', '알림', wx.OK)
            self.txtName.SetFocus()
            return
        
        self.LoginCheck()
        
    
    def LoginCheck(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
                
            no = self.txtNo.GetValue()
            name = self.txtName.GetValue()
                
            sql = '''
                select count(jikwon_no) as count 
                from jikwon
                where jikwon_no='{}' and jikwon_name='{}' 
            '''.format(no, name)
                
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            
            if count <= 0:
                wx.MessageBox('로그인 실패', '알림', wx.OK)
                return
            else:
                self.staMsg.SetLabelText(no + '번 직원의 관리고객 목록')
                self.DisplayData(no)   #로그인 성공시 출력

        except Exception as e:
            print('LoginCheck error :', e)
              
        finally:
            cursor.close()
            conn.close()

    
    def DisplayData(self, no): #ListCtrl로 출력
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = '''
                select gogek_no, gogek_name, gogek_tel
                from gogek
                where gogek_damsano={}
            '''.format(no)
            
            cursor.execute(sql)
            datas = cursor.fetchall()
            
            self.lstGogek.DeleteAllItems() #출력 전에 초기화
            for no, name, tel in datas:
                i = self.lstGogek.InsertItem(len(datas), 0)   #InsertItem(최대 행수, 열수)
                self.lstGogek.SetItem(i, 0, str(no)) #고객 번호
                self.lstGogek.SetItem(i, 1, name)   #고객명
                self.lstGogek.SetItem(i, 2, tel)       #고객 번호
            
            self.staCount.SetLabelText('인원수 : ' + str(len(datas)))
                
        except Exception as e:
            print('DisplayData error :', e)
            
        finally:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop() #무한루프