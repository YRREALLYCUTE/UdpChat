# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class AddGroupDlg
###########################################################################

class AddGroupDlg(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(378, 76), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gbSizer8 = wx.GridBagSizer(0, 0)
        gbSizer8.SetFlexibleDirection(wx.BOTH)
        gbSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        gbSizer8.Add(self.m_staticText10, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.username_input_dlg = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.username_input_dlg, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        self.confirm_btn_dlg = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.confirm_btn_dlg, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.cancel_btn_dlg = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.cancel_btn_dlg, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.SetSizer(gbSizer8)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.confirm_btn_dlg.Bind(wx.EVT_BUTTON, self.add_group)
        self.cancel_btn_dlg.Bind(wx.EVT_BUTTON, self.cancel)

        self.group_name = ''

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def add_group(self, event):
        self.group_name = self.username_input_dlg.GetValue()
        self.Close()

    def cancel(self, event):
        self.Close()

    def get_group_name(self):
        return self.group_name