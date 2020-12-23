# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from socket import *
import utils
from datetime import datetime
import AddFriendDlg
import AddGroupDlg

###########################################################################
## 常量
SERVER_PORT = 7215
SERVER_HOST = '192.168.190.206'
###########################################################################

###########################################################################
## Class Client
###########################################################################


class Client(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"聊天程序客户端", pos=wx.DefaultPosition, size=wx.Size(648, 452),
                          style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        gbSizer6 = wx.GridBagSizer(0, 0)
        gbSizer6.SetFlexibleDirection(wx.BOTH)
        gbSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText4 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"用户名", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        gbSizer6.Add(self.m_staticText4, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.username_input = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        gbSizer6.Add(self.username_input, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText5 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"密码", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        gbSizer6.Add(self.m_staticText5, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.pwd_input = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_PASSWORD)
        gbSizer6.Add(self.pwd_input, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.loginBtn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer6.Add(self.loginBtn, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.logoutBtn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"注销", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer6.Add(self.logoutBtn, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.signBtn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer6.Add(self.signBtn, wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.ALL, 5)

        self.addFriendBtn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"添加朋友", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        gbSizer6.Add(self.addFriendBtn, wx.GBPosition(1, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.encryptMsg = wx.CheckBox(sbSizer2.GetStaticBox(), wx.ID_ANY, u"加密聊天信息", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.encryptMsg.SetValue(True)
        gbSizer6.Add(self.encryptMsg, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.loginStatus = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"登录状态：离线", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_RIGHT)
        self.loginStatus.Wrap(-1)

        gbSizer6.Add(self.loginStatus, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.addGroupBtn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"加入群聊", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer6.Add(self.addGroupBtn, wx.GBPosition(1, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.clearBtn = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"清空消息", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer6.Add(self.clearBtn, wx.GBPosition(1, 6), wx.GBSpan(1, 1), wx.ALL, 5)

        sbSizer2.Add(gbSizer6, 1, wx.EXPAND, 5)

        bSizer3.Add(sbSizer2, 2, wx.EXPAND, 5)

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"用户列表"), wx.VERTICAL)

        self.userTree = wx.TreeCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TR_DEFAULT_STYLE)
        sbSizer4.Add(self.userTree, 1, wx.ALL | wx.EXPAND, 5)

        gbSizer2.Add(sbSizer4, wx.GBPosition(0, 0), wx.GBSpan(12, 20), wx.EXPAND, 5)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"消息"), wx.VERTICAL)

        self.message = wx.TextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        sbSizer5.Add(self.message, 1, wx.ALL | wx.EXPAND, 5)

        gbSizer2.Add(sbSizer5, wx.GBPosition(0, 20), wx.GBSpan(12, 45), wx.EXPAND, 5)

        bSizer3.Add(gbSizer2, 4, wx.EXPAND, 5)

        sbSizer12 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        gbSizer5 = wx.GridBagSizer(0, 0)
        gbSizer5.SetFlexibleDirection(wx.BOTH)
        gbSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.msgInput = wx.TextCtrl(sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, wx.TE_PROCESS_ENTER)
        gbSizer5.Add(self.msgInput, wx.GBPosition(0, 0), wx.GBSpan(1, 52), wx.ALL | wx.EXPAND | wx.ALIGN_BOTTOM, 5)

        self.sendBtn = wx.Button(sbSizer12.GetStaticBox(), wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer5.Add(self.sendBtn, wx.GBPosition(0, 53), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer12.Add(gbSizer5, 1, wx.EXPAND, 5)

        bSizer3.Add(sbSizer12, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(5, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        self.recv_timer = wx.Timer()
        self.recv_timer.SetOwner(self, wx.ID_ANY)
        # self.send_timer = wx.Timer()
        # self.send_timer.SetOwner(self, wx.ID_ANY)

        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        # 设置为异步模式
        self.udp_socket.setblocking(False)

        # self.client_port = self.udp_socket.getsockname()[1]
        # self.client_ip = self.udp_socket.getsockname()[0]
        self.server_dest = (SERVER_HOST, SERVER_PORT)
        ip = gethostbyname(gethostname())
        # todo 获取本机的IP地址
        self.udp_socket.bind((ip, 0))

        # 消息列表 {user1: '', user2: '', user3: ''} 消息以文本的形式存储
        self.message_dic = {}
        # 未读消息数 ( user1: 1, user2: 2 }
        self.miss_message_dic = {}
        # 未读消息总数
        self.count_miss = 0
        # 登录用户
        self.login_user = None
        # 登录状态
        self.login_state = False
        # 联系人列表
        self.root = self.userTree.AddRoot('联系人列表')
        self.friend_list = self.userTree.AppendItem(self.root, '好友列表')
        self.group_list = self.userTree.AppendItem(self.root, '群组列表')
        # 正在进行的联系人
        self.contacting = ''
        # Connect Events
        self.loginBtn.Bind(wx.EVT_BUTTON, self.login)
        self.logoutBtn.Bind(wx.EVT_BUTTON, self.logout)
        self.signBtn.Bind(wx.EVT_BUTTON, self.sign)
        self.addFriendBtn.Bind(wx.EVT_BUTTON, self.addFriend)
        self.addGroupBtn.Bind(wx.EVT_BUTTON, self.addGroup)
        self.clearBtn.Bind(wx.EVT_BUTTON, self.clear)
        self.msgInput.Bind(wx.EVT_TEXT_ENTER, self.sendMsg)
        self.sendBtn.Bind(wx.EVT_BUTTON, self.sendMsg)
        self.Bind(wx.EVT_TIMER, self.recvMsg, self.recv_timer)
        self.userTree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.get_user_message)
        # self.send_timer.Bind(wx.EVT_TIMER, self.send_timer)
        self.recv_timer.Start()

    def __del__(self):
        pass

    #########################################################
    ## -n  新用户注册     -n username
    ## -t  发送消息       message -t username
    ## -ta 广播/公告     -ta message
    ## -tg 群聊          message -tg group
    ## -l  用户登录      username -l password
    ## -fl 好友列表      -fl username
    ## -gl 群组列表      -gl username
    ## -af 添加好友      -af username
    ## -ag 添加群组      -ag groupname
    #########################################################

    # Virtual event handlers, overide them in your derived class
    def login(self, event):
        # 获取输入的用户名和密码
        username = self.username_input.GetValue()
        password = self.pwd_input.GetValue()
        if self.login_state:
            dlg = wx.MessageDialog(None, u'您已经登录了！', u'信息', wx.YES_DEFAULT|wx.ICON_ERROR)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            else:
                dlg.Destroy()
            return
        if username == '' or password == '':
            dlg = wx.MessageDialog(None, u'请输入用户名和密码！', u'信息', wx.YES_DEFAULT | wx.ICON_ERROR)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            else:
                dlg.Destroy()
            return

        data_info = username + " -l " + password

        if not self.recv_timer.IsRunning():
            self.recv_timer.Start()

        # 发送到服务器端，进行验证
        self.udp_socket.sendto(data_info.encode('gb2312'), self.server_dest)
        event.Skip()

    def logout(self, event):
        if not self.login_state:
            dlg = wx.MessageDialog(None, u"您还没有登陆", u"错误", wx.YES_DEFAULT|wx.ICON_ERROR)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            return
        logout_cmd = 'exit'
        self.udp_socket.sendto(logout_cmd.encode('gb2312'), self.server_dest)

    def sign(self, event):
        username = self.username_input.GetValue()
        password = self.pwd_input.GetValue()
        data_info = username + " -n " + password

        # 发送到服务器端
        self.udp_socket.sendto(data_info.encode('gb2312'), self.server_dest)
        event.Skip()

    def addFriend(self, event):
        dlg = AddFriendDlg.AddFriendDlg(self)
        dlg.ShowModal()
        friend_name = dlg.get_friend_name()
        if friend_name == '':
            return

        add_friend_cmd = '-af %s' % friend_name
        self.udp_socket.sendto(add_friend_cmd.encode("gb2312"), self.server_dest)
        event.Skip()

    def addGroup(self, event):
        dlg = AddGroupDlg.AddGroupDlg(self)
        dlg.ShowModal()
        group_name = dlg.get_group_name()
        if group_name == '':
            return

        add_group_cmd = '-ag %s' % group_name
        self.udp_socket.sendto(add_group_cmd.encode("gb2312"), self.server_dest)
        event.Skip()

    def clear(self, event):
        self.message.Clear()

    def sendMsg(self, event):
        data_info = self.msgInput.GetValue()

        item = self.userTree.GetSelection()
        msg_window_name = self.userTree.GetItemText(item)

        # 如果当前选择的不是好友，那么给出提示
        if msg_window_name == '联系人列表' or msg_window_name == '好友列表' or msg_window_name == '群组列表':
            dlg = wx.MessageDialog(None, u"请选中一个联系人", u"提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            else:
                dlg.Destroy()
            return
        if self.userTree.GetItemText(self.userTree.GetItemParent(item)) == '好友列表':
            # 显示在当前聊天窗口中
            self.message.write(utils.add_message(data_info, '你'))
            self.message_dic[msg_window_name] = self.message_dic[msg_window_name] + utils.add_message(data_info, '你')

            cmd_to_server = "%s -t %s" % (data_info, msg_window_name)
            if self.encryptMsg.GetValue():
                enc_cmd = utils.encrypt_msg(cmd_to_server)
                self.udp_socket.sendto(enc_cmd, self.server_dest)
            else:
                self.udp_socket.sendto(cmd_to_server.encode('gb2312'), self.server_dest)
        elif self.userTree.GetItemText(self.userTree.GetItemParent(item)) == '群组列表':
            cmd_to_server = "%s -tg %s" % (data_info, msg_window_name)
            if self.encryptMsg.GetValue():
                enc_cmd = utils.encrypt_msg(cmd_to_server)
                self.udp_socket.sendto(enc_cmd, self.server_dest)
            else:
                self.udp_socket.sendto(cmd_to_server.encode('gb2312'), self.server_dest)
        self.msgInput.Clear()
        event.Skip()

    def recvMsg(self, event):
        # 显示当前时间
        self.SetStatusText(datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 4)
        # 显示未读消息数量
        self.SetStatusText("未读消息：%d" % self.count_miss, 1)
        try:
            recv_data, dest_ip = self.udp_socket.recvfrom(1024)
        except:
            event.Skip()
        else:
            if recv_data.decode("gb2312") == 'exit' and dest_ip == self.server_dest:
                self.message.write(utils.add_log('已经退出登录'))
                self.loginStatus.Label = '登录状态：离线'
                self.SetStatusText("已离线", 0)
                self.SetStatusText("", 1)
                self.SetStatusText("", 2)
                self.SetStatusText("", 3)
                self.userTree.DeleteChildren(self.friend_list)
                self.userTree.DeleteChildren(self.group_list)

                # 消息列表 {user1: '', user2: '', user3: ''} 消息以文本的形式存储
                self.message_dic = {}
                # 未读消息数 ( user1: 1, user2: 2 }
                self.miss_message_dic = {}
                # 未读消息总数
                self.count_miss = 0
                # 登录用户
                self.login_user = None
                # 登录状态
                self.login_state = False

                self.recv_timer.Stop()
            else:
                list_info = recv_data.decode("gb2312").split(' ')
                if list_info[-2] == '-rt':
                    # 发送消息响应 返回格式 message -rt send_username
                    username = list_info[-1]
                    message = ' '.join(list_info[:-2])

                    if username == '系统':
                        self.message.write(utils.add_log(message))
                        return
                    if self.contacting != username:
                        self.count_miss += 1

                    if username not in self.message_dic.keys():
                        self.message_dic[username] = utils.add_message(message, username)
                        if self.contacting != username:
                            self.miss_message_dic[username] = 1
                    else:
                        self.message_dic[username] = self.message_dic[username] + utils.add_message(message, username)
                        if self.contacting != username:
                            self.miss_message_dic[username] = self.miss_message_dic[username] + 1

                    # 如果当前聊天窗口就是正在的窗口，直接将消息加入到窗口中
                    if self.contacting == username:
                        self.message.write(utils.add_message(message, username))
                elif list_info[-2] == '-rtg':
                    # 发送消息响应 返回格式 message username -rt group_name
                    group_name = list_info[-1]
                    username = list_info[-3]
                    message = ' '.join(list_info[:-3])

                    if group_name == '系统':
                        self.message.write(utils.add_log(message))
                        return
                    if self.contacting != group_name:
                        self.count_miss += 1

                    if group_name not in self.message_dic.keys():
                        self.message_dic[group_name] = utils.add_message(message, username + "-" + group_name)
                        if self.contacting != group_name:
                            self.miss_message_dic[group_name] = 1
                    else:
                        self.message_dic[group_name] = self.message_dic[group_name] + utils.add_message(message, username + "-" + group_name)
                        if self.contacting != group_name:
                            self.miss_message_dic[group_name] = self.miss_message_dic[group_name] + 1

                    # 如果当前聊天窗口就是正在的窗口，直接将消息加入到窗口中
                    if self.contacting == group_name:
                        self.message.write(utils.add_message(message, username + "-" + group_name))
                elif list_info[-2] == '-rl':
                    # 登录响应 返回格式 message -rl username
                    username = list_info[-1]
                    message = ' '.join(list_info[:-2])
                    if message == '登录成功！':
                        # 修改在线用户状态
                        self.login_state = True
                        self.login_user = username
                        self.message.write(utils.add_log(message))
                        self.SetStatusText("%s 已登录" % username, 0)
                        self.loginStatus.Label = "登陆状态：在线"
                        # todo 获取联系人列表
                        friend_cmd = "-fl %s" % username
                        self.udp_socket.sendto(friend_cmd.encode("gb2312"), self.server_dest)
                        group_cmd = "-gl %s" % username
                        self.udp_socket.sendto(group_cmd.encode("gb2312"), self.server_dest)
                    else:
                        self.message.write(utils.add_log(message))
                elif list_info[-2] == '-rn':
                    # 注册响应 返回格式 -rn message
                    msg = list_info[-1]
                    dlg = wx.MessageDialog(None, u"%s" % msg, u'信息', wx.YES_NO | wx.ICON_WARNING)
                    if dlg.ShowModal() == wx.ID_YES:
                        dlg.Destroy()
                    else:
                        dlg.Destroy()
                elif list_info[-2] == '-rfl':
                    # 好友列表响应 返回格式 f1 f2 f3 ... -rfl fcount
                    fcount = int(list_info[-1])
                    self.userTree.DeleteChildren(self.friend_list)
                    for i in range(fcount):
                        self.userTree.AppendItem(self.friend_list, list_info[i])
                    self.SetStatusText("好友数量：%d" % fcount, 2)
                elif list_info[-2] == '-rgl':
                    # 群组列表响应 返回格式 g1 g2 g3 ... -rgl gcount
                    gcount = int(list_info[-1])
                    self.userTree.DeleteChildren(self.group_list)
                    for i in range(gcount):
                        self.userTree.AppendItem(self.group_list, list_info[i])
                    self.SetStatusText("群组数量：%d" % gcount, 3)
                elif list_info[-2] == '-maf':
                    # 响应添加好友请求 格式 -maf username // username为请求添加您为好友的用户名称
                    username = list_info[-1]
                    dlg = wx.MessageDialog(None, u'%s 请求添加您为好友' % username, u'好友请求', wx.YES_NO | wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_YES:
                        # 同意好友请求
                        self.udp_socket.sendto(('%s -rmaf agree' % username).encode('gb2312'), self.server_dest)
                    else:
                        # 拒绝好友请求
                        self.udp_socket.sendto(('%s -rmaf disagree' % username).encode('gb2312'), self.server_dest)
                elif list_info[-2] == '-rag':
                    if list_info[-1] == 'success':
                        self.message.write(utils.add_log("添加成功！"))
                        self.udp_socket.sendto(("-gl %s" % list_info[-3]).encode('gb2312'), self.server_dest)
                elif list_info[-3] == '-raf':
                    # 添加好友响应 返回格式 f1 f2 f3 ... -raf fcount message
                    message = list_info[-1]
                    if message != '添加成功！':
                        dlg = wx.MessageDialog(None, u'%s' % message, u'信息', wx.YES_NO | wx.ICON_QUESTION)
                        if dlg.ShowModal() == wx.ID_YES:
                            dlg.Destroy()
                        else:
                            dlg.Destroy()
                    else:
                        self.message.write(utils.add_log(list_info[-1]))

                        fcount = int(list_info[-2])
                        self.userTree.DeleteChildren(self.friend_list)
                        for i in range(fcount):
                            self.userTree.AppendItem(self.friend_list, list_info[i])
                        self.SetStatusText("好友数量：%d" % fcount, 2)
                # self.message.write(str(recv_data.decode("gb2312")))

            print(recv_data.decode("gb2312"))

            event.Skip()
        event.Skip()

    def get_user_message(self, event):
        item = event.GetItem()
        item_text = self.userTree.GetItemText(item)
        if item_text == '联系人列表' or item_text == '好友列表' or item_text == '群组列表':
            return
        elif self.userTree.GetItemText(self.userTree.GetItemParent(item)) == '好友列表':
            friend_name = item_text
            self.contacting = friend_name
            if friend_name not in self.message_dic.keys():
                self.message_dic[friend_name] = ''
                self.miss_message_dic[friend_name] = 0
            message_all = self.message_dic[friend_name]
            self.count_miss -= self.miss_message_dic[friend_name]
            self.message.Clear()
            self.message.write(message_all)

            self.miss_message_dic[friend_name] = 0
            self.SetStatusText("未读消息：%d" % self.count_miss, 1)
        elif self.userTree.GetItemText(self.userTree.GetItemParent(item)) == '群组列表':
            group_name = item_text
            self.contacting = group_name
            if group_name not in self.message_dic.keys():
                self.message_dic[group_name] = ''
                self.miss_message_dic[group_name] = 0
            message_all = self.message_dic[group_name]
            self.count_miss -= self.miss_message_dic[group_name]
            self.message.Clear()
            self.message.write(message_all)

            self.miss_message_dic[group_name] = 0
            self.SetStatusText("未读消息：%d" % self.count_miss, 1)
        event.Skip()