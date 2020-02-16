#-*- coding: utf-8 -*-
import wx
from HelloFrame import HelloFrame



app = wx.App()
frm = HelloFrame(None, title='Hello Frame', size=(500,200))
frm.Show()
app.MainLoop()