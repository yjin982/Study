import wx
import wx.xrc
import MySQLdb
import ast

#db연결정보 읽기
with open('mariadb.txt', 'r') as f:
    config = ast.literal_eval(f.read())
    

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetBackgroundColour( wx.Colour( 253, 242, 255 ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"번호 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.txtNo = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtNo, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.btnInsert = wx.Button( self.m_panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        bSizer2.Add( self.btnInsert, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"이름 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtName, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.btnUpdate = wx.Button( self.m_panel2, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btnUpdate, 0, wx.ALL, 5 )
        
        self.btnConfirm = wx.Button( self.m_panel2, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btnConfirm, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"전화 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.txtTel = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtTel, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.btnDelete = wx.Button( self.m_panel3, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        bSizer4.Add( self.btnDelete, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lstMem = wx.ListCtrl( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer5.Add( self.lstMem, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticText = wx.StaticText( self.m_panel5, wx.ID_ANY, u"인원수 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText.Wrap( -1 )
        bSizer6.Add( self.staticText, 0, wx.ALL, 5 )
        
        self.staCount = wx.StaticText( self.m_panel5, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer6.Add( self.staCount, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer6 )
        self.m_panel5.Layout()
        bSizer6.Fit( self.m_panel5 )
        bSizer1.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.lstMem.InsertColumn(0, '번호', width=60)
        self.lstMem.InsertColumn(1, '이름', width=100)
        self.lstMem.InsertColumn(2, '전화', width=150)
        
        # Connect Events
        self.btnInsert.Bind( wx.EVT_BUTTON, self.onBtnClick )
        self.btnUpdate.Bind( wx.EVT_BUTTON, self.onBtnClick )
        self.btnConfirm.Bind( wx.EVT_BUTTON, self.onBtnClick )
        self.btnDelete.Bind( wx.EVT_BUTTON, self.onBtnClick )
        
        self.btnInsert.id = 1
        self.btnUpdate.id = 2
        self.btnConfirm.id = 3
        self.btnDelete.id = 4
        
        self.btnConfirm.Enable(enable=False)
        
        self.ViewListData()
    
    def __del__( self ):
        pass
    
    def ViewListData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            self.lstMem.DeleteAllItems()
            
            sql = 'select * from pymem'
            cursor.execute(sql)
            
            count = 0
            for data in cursor:
                i = self.lstMem.InsertItem(655535, 0)
                self.lstMem.SetItem(i, 0, str(data[0]))
                self.lstMem.SetItem(i, 1, str(data[1]))
                self.lstMem.SetItem(i, 2, str(data[2]))
                count += 1
            self.staCount.SetLabelText(str(count))
        
        except Exception as e:
            print('ViewListData error :', e)
        finally:
            cursor.close()
            conn.close()
    
    # Virtual event handlers, overide them in your derived class
    def onBtnClick( self, event ):
        id = event.GetEventObject().id
        
        if id == 1:
            self.MemInsert()        #등록
        elif id == 2:
            self.MemUpdate()      #수정 준비
        elif id == 3:
            self.MemUpdateOk()  #수정 처리
        elif id == 4:
            self.MemDelete()      #삭제 처리
        elif id == 5:
            self.MemUpdateCancel() #수정 취소
    
    
    def MemInsert(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if no == '' or name == '' or tel == '':
            wx.MessageBox('자료를 입력하세요', '입력', wx.OK)
            return
        else:
            try:
                conn = MySQLdb.connect(**config)
                cursor = conn.cursor()
                data = self.SelectData(no) #추가용 번호의 등록 가능 여부 판단
                
                #번호 중복일시
                if data != None:
                    wx.MessageBox('이미 사용 중인 번호입니다', '알림', wx.OK)
                    self.txtNo.SetFocus()
                    return
                
                #번호 중복 아닐시 추가 계속
                sql = 'insert into pymem values(%s, %s, %s)'
                result = cursor.execute(sql, (no, name, tel))
                
                if result == 1:
                    conn.commit()
                    self.ViewListData() #추가후 자료 보기
                    self.txtNo.SetValue('') #입력 자료 초기화
                    self.txtName.SetValue('')
                    self.txtTel.SetValue('')
                else:
                    conn.rollback()
                    return                
            except Exception as e:
                print('Insert error :', e)
                conn.rollback()
            finally:
                cursor.close()
                conn.close()     
    
    def SelectData(self, no): #해당 번호의 자료 읽기(i, u, d에서 사용)
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = 'select * from pymem where bun={}'.format(no)
            cursor.execute(sql)
            
            data = cursor.fetchone()
            return data
        
        except Exception as e:
            print('SelectData error :', e)
        finally:
            cursor.close()
            conn.close()  
    
    def MemUpdate(self):
        dlg = wx.TextEntryDialog(None, '수정할 번호 입력', '수정')
        if dlg.ShowModal() == wx.ID_OK:
            
            if dlg.GetValue == '':
                return
            
            upno = dlg.GetValue()
            data = self.SelectData(upno)
            
            if data == None:
                wx.MessageBox(upno + '번은 등록된 자료가 아닙니다.', '알림', wx.ID_OK)
                return
            
            #수정할 자료를 화면에 표시
            self.txtNo.SetValue(str(data[0]))
            self.txtName.SetValue(str(data[1]))
            self.txtTel.SetValue(str(data[2]))
            self.txtNo.SetEditable(False) #번호는 수정불가
            self.btnConfirm.Enable(True) #확인 버튼 활성화
            self.btnUpdate.SetLabelText('취소')
            self.btnUpdate.id = 5 #버튼 아이디 동적 부여
        else:
            return
        dlg.Destroy()
    
    def MemUpdateOk(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if name == '':
            wx.MessageBox('자료를 입력하세요', '입력', wx.OK)
            return
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = 'update pymem set irum=%s, junhwa=%s where bun=%s'
            cursor.execute(sql, (name, tel, no))
            conn.commit()
            
            self.ViewListData() #수정후 자료 보기
            self.txtNo.SetValue('')
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
            self.txtNo.SetEditable(True)
            self.btnUpdate.SetLabelText('수정')
            self.btnUpdate.id = 2
            self.btnConfirm.Enable(False)
        except Exception as e:
            print('MemUpdateOk error :', e)
        finally:
            cursor.close()
            conn.close()  
    
    def MemDelete(self):
        dlg = wx.TextEntryDialog(None, '삭제할 번호 입력', '삭제')
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue == '':
                return
            
            delno = dlg.GetValue()
            data = self.SelectData(delno)
            if data == None:
                wx.MessageBox(delno + '번은 등록된 자료가 아닙니다.', '알림', wx.ID_OK)
                return
            
            #삭제 준비 계속
            try:
                conn = MySQLdb.connect(**config)
                cursor = conn.cursor()
                sql = 'delete from pymem where bun={}'.format(delno)
                cursor.execute(sql)
                conn.commit()
                
                self.ViewListData() #삭제 후 자료보기
            except Exception as e:
                print('MemDelete error :', e)
                conn.rollback()
            finally:
                cursor.close()
                conn.close()  
    
    def MemUpdateCancel(self):
        self.ViewListData() #수정후 자료 보기
        self.txtNo.SetValue('')
        self.txtName.SetValue('')
        self.txtTel.SetValue('')
        self.txtNo.SetEditable(True)
        self.btnUpdate.SetLabelText('수정')
        self.btnUpdate.id = 2
        self.btnConfirm.Enable(False)
    
if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop() 