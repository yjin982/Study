import wx
import wx.xrc

class MyCalc ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"간단 계산기", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText11 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"숫자 1 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer7.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        self.txtNum1 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.txtNum1, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel4.SetSizer( bSizer7 )
        self.m_panel4.Layout()
        bSizer7.Fit( self.m_panel4 )
        bSizer5.Add( self.m_panel4, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText12 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"숫자 2 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer8.Add( self.m_staticText12, 0, wx.ALL, 5 )
        
        self.txtNum2 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.txtNum2, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer8 )
        self.m_panel5.Layout()
        bSizer8.Fit( self.m_panel5 )
        bSizer5.Add( self.m_panel5, 0, wx.EXPAND|wx.ALL, 5 )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        rdoOpChoices = [ u"+", u"-", u"*", u"/" ]
        self.rdoOp = wx.RadioBox( self.m_panel6, wx.ID_ANY, u"연산자 선택 :", wx.DefaultPosition, wx.DefaultSize, rdoOpChoices, 1, wx.RA_SPECIFY_ROWS )
        self.rdoOp.SetSelection( 0 )
        bSizer9.Add( self.rdoOp, 1, wx.ALL, 5 )
        
        
        self.m_panel6.SetSizer( bSizer9 )
        self.m_panel6.Layout()
        bSizer9.Fit( self.m_panel6 )
        bSizer5.Add( self.m_panel6, 0, wx.EXPAND|wx.ALL, 5 )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText14 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"결과 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        bSizer10.Add( self.m_staticText14, 0, wx.ALL, 5 )
        
        self.staResult = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staResult.Wrap( -1 )
        bSizer10.Add( self.staResult, 1, wx.ALL, 5 )
        
        
        self.m_panel7.SetSizer( bSizer10 )
        self.m_panel7.Layout()
        bSizer10.Fit( self.m_panel7 )
        bSizer5.Add( self.m_panel7, 1, wx.EXPAND|wx.ALL, 5 )
        
        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btnCalc = wx.Button( self.m_panel8, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btnCalc, 1, wx.ALL, 5 )
        self.btnCalc.id = 1
        
        self.btnClear = wx.Button( self.m_panel8, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btnClear, 1, wx.ALL, 5 )
        self.btnClear.id = 2
        
        self.btnExit = wx.Button( self.m_panel8, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btnExit, 1, wx.ALL, 5 )
        self.btnExit.id = 3
        
        self.m_panel8.SetSizer( bSizer11 )
        self.m_panel8.Layout()
        bSizer11.Fit( self.m_panel8 )
        bSizer5.Add( self.m_panel8, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnCalc.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btnClear.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btnExit.Bind( wx.EVT_BUTTON, self.OnProcess )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnProcess( self, event ):
        op = self.rdoOp.GetStringSelection()
        bid = event.GetEventObject().id
        num1 = self.txtNum1.GetValue()
        num2 = self.txtNum2.GetValue()
        
        if bid == 1:
            if num1.isdecimal() and num2.isdecimal():
                num1 = int(num1)
                num2 = int(num2)
                
                if op == '+':
                    re = num1 + num2
                    self.staResult.SetLabelText(str(re))
                elif op == '-':
                    re = num1 - num2
                    self.staResult.SetLabelText(str(re))
                elif op == '*':
                    re = num1 * num2
                    self.staResult.SetLabelText(str(re))
                elif op == '/':
                    try:
                        re = num1 / num2
                        self.staResult.SetLabelText(str(re))
                    except Exception:
                        msgDial = wx.MessageDialog(self, '0으로 나눌 수 없습니다.', '경고', wx.OK)
                        msgDial.ShowModal()
                        msgDial.Destroy()
            else:
                msgDial = wx.MessageDialog(self, '숫자를 입력하세요', '경고', wx.OK)
                msgDial.ShowModal()
                msgDial.Destroy()
                
        elif bid == 2:
            self.txtNum1.SetLabelText('')
            self.txtNum2.SetLabelText('')
            self.staResult.SetLabelText('')
            self.rdoOp.SetSelection(0)
            
        else:
            msgDial = wx.MessageBox('종료하시겠습니까?', '종료', wx.YES_NO)
            
            if(msgDial == wx.ID_YES):
                msgDial.Destroy()
                self.Close()
        

if __name__ == '__main__':
    app = wx.App()
    MyCalc(None).Show()
    app.MainLoop() #무한루프