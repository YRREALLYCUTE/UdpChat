# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
from socket import *
from threading import Thread
from datetime import datetime
import utils
import User
import Group

##########################################################################
## Const
###########################################################################
MAX = 100  # 最大监听队列  超过之后服务器不再接受请求
ip_user_dic = {}  # 在线用户列表 {ip: user, ip: user}
user_login_dic = {}  # 在线用户列表 {username: ip, username: ip}
user_login_time_dic = {} # 在线用户列表 { username: date_time, username: datetime}

# 端口号和主机地址
PORT = 7215
HOST = gethostbyname(gethostname())


###########################################################################
## Class Server
###########################################################################

class Server(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"聊天程序服务器", pos=wx.DefaultPosition, size=wx.Size(615, 461),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"登录用户列表"), wx.VERTICAL)

        self.login_user_Grid = wx.grid.Grid(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.login_user_Grid.CreateGrid(5, 2)
        self.login_user_Grid.EnableEditing(True)
        self.login_user_Grid.EnableGridLines(True)
        self.login_user_Grid.EnableDragGridSize(False)
        self.login_user_Grid.SetMargins(0, 0)

        # Columns
        self.login_user_Grid.SetColSize(0, 120)
        self.login_user_Grid.SetColSize(1, 120)
        self.login_user_Grid.EnableDragColMove(False)
        self.login_user_Grid.EnableDragColSize(True)
        self.login_user_Grid.SetColLabelSize(25)
        self.login_user_Grid.SetColLabelValue(0, u"用户名")
        self.login_user_Grid.SetColLabelValue(1, u"登录时间")
        self.login_user_Grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.login_user_Grid.EnableDragRowSize(True)
        self.login_user_Grid.SetRowLabelSize(30)
        self.login_user_Grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.login_user_Grid.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        sbSizer4.Add(self.login_user_Grid, 1, wx.ALL | wx.EXPAND, 5)

        gbSizer2.Add(sbSizer4, wx.GBPosition(0, 0), wx.GBSpan(12, 30), wx.EXPAND, 5)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"群聊列表"), wx.VERTICAL)

        self.group_grid = wx.grid.Grid(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.group_grid.CreateGrid(5, 2)
        self.group_grid.EnableEditing(True)
        self.group_grid.EnableGridLines(True)
        self.group_grid.EnableDragGridSize(False)
        self.group_grid.SetMargins(0, 0)

        # Columns
        self.group_grid.SetColSize(0, 129)
        self.group_grid.SetColSize(1, 129)
        self.group_grid.EnableDragColMove(False)
        self.group_grid.EnableDragColSize(True)
        self.group_grid.SetColLabelSize(25)
        self.group_grid.SetColLabelValue(0, u"群聊名称")
        self.group_grid.SetColLabelValue(1, u"群内成员")
        self.group_grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.group_grid.EnableDragRowSize(True)
        self.group_grid.SetRowLabelSize(30)
        self.group_grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.group_grid.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        sbSizer5.Add(self.group_grid, 1, wx.ALL | wx.EXPAND, 5)

        gbSizer2.Add(sbSizer5, wx.GBPosition(0, 30), wx.GBSpan(12, 32), wx.EXPAND, 5)

        bSizer3.Add(gbSizer2, 1, wx.EXPAND, 5)

        sbSizer14 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"日志"), wx.VERTICAL)

        self.log_text = wx.TextCtrl(sbSizer14.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        sbSizer14.Add(self.log_text, 1, wx.ALL | wx.EXPAND, 5)

        bSizer3.Add(sbSizer14, 3, wx.EXPAND, 5)

        gbSizer7 = wx.GridBagSizer(0, 0)
        gbSizer7.SetFlexibleDirection(wx.BOTH)
        gbSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.start_btn = wx.Button(self, wx.ID_ANY, u"开启", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.start_btn, wx.GBPosition(0, 8), wx.GBSpan(1, 5),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.stop_btn = wx.Button(self, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer7.Add(self.stop_btn, wx.GBPosition(0, 36), wx.GBSpan(1, 5),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.ALIGN_RIGHT, 5)

        bSizer3.Add(gbSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()
        self.m_statusBar2 = self.CreateStatusBar(3, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        self.recv_timer = wx.Timer()
        self.recv_timer.SetOwner(self, wx.ID_ANY)
        self.send_timer = wx.Timer()
        self.send_timer.SetOwner(self, wx.ID_ANY)

        # 初始化状态栏
        self.SetStatusText("在线人数：%d" % user_login_dic.__len__(), 0)
        self.SetStatusText("IP地址：%s" % HOST, 1)
        self.SetStatusText("端口号：%d" % PORT, 2)

        # 加载系统的用户和用户群组
        self.users = utils.get_user()
        self.groups = utils.get_group()

        # socket SOCK_DGRAM ==> UDP
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        # 设置为异步模式
        self.udp_socket.setblocking(False)
        self.udp_socket.bind((HOST, PORT))

        self.__server_open__ = False

        self.Bind(wx.EVT_TIMER, self.recv_msg, self.recv_timer)
        self.Bind(wx.EVT_TIMER, self.send_msg, self.send_timer)
        # Connect Events
        self.start_btn.Bind(wx.EVT_BUTTON, self.start)
        self.stop_btn.Bind(wx.EVT_BUTTON, self.stop)

        self.log_text.write(utils.add_log("服务器未启动，请点击下方按钮启动服务器..."))

    #########################################################
    ## -n  新用户注册     -n username
    ## -t  发送消息       message -t username
    ## -tg 群聊          message -tg group
    ## -l  用户登录      username -l password
    ## -fl 好友列表      -fl username
    ## -gl 群组列表      -gl username
    ## -af 添加好友      -af username
    ## -ag 添加群组      -ag groupname
    #########################################################
    def __del__(self):
        pass

    def start(self, event):
        if not self.__server_open__:
            self.recv_timer.Start()
            self.send_timer.Start()
            self.flush_groups_list()
            self.log_text.write(utils.add_log("服务器已经启动！"))
            self.__server_open__ = True
        else:
            dlg = wx.MessageDialog(None, u'服务器已经启动',u'警告', wx.YES_DEFAULT|wx.ICON_WARNING)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()

    def recv_msg(self, event):
        try:
            recv_data, dest_ip = self.udp_socket.recvfrom(1024)
        except:
            event.Skip()
        else:
            # self.log_text.write(utils.add_log(recv_data))
            # print(dest_ip)
            try:
                info_list = str(recv_data.decode("gb2312")).split(' ')
            except:
                info_list = utils.decrypt_msg(recv_data).split(' ')
            # 注销请求
            if info_list[0] == 'exit':
                self.udp_socket.sendto('exit'.encode('gb2312'), dest_ip)

                name = ip_user_dic.pop(dest_ip)
                user_login_dic.pop(name)
                user_login_time_dic.pop(name)
                self.flush_login_user_list()
                self.log_text.write(utils.add_log("用户 %s 已经退出聊天" % name))
            # 发送消息
            elif info_list[-2] == '-t':
                # 判断目标是否为注册用户

                flag = False
                # 判断目标用户是否为当前用户的好友
                username = ip_user_dic[dest_ip]
                for user in self.users:
                    if user.get_username() == username:
                        friend_list = user.get_friend()
                        for friend in friend_list:
                            if friend.get_username() == info_list[-1]:
                                flag = True

                # 目标用户咩有登录
                if info_list[-1] not in user_login_dic.keys():
                    msg = "发送失败！用户未登录！"
                    self.udp_socket.sendto(("%s -rt %s" % (msg, "系统")).encode("gb2312"), dest_ip)
                    return

                dest_user_ip = user_login_dic[info_list[-1]]
                if flag:
                    msg = ' '.join(info_list[:-2])
                    send_user = ip_user_dic[dest_ip]
                else:
                    msg = ' '.join(info_list[:-2]) + "\r\n[该用户不是您的好友，请谨慎]"
                    send_user = ip_user_dic[dest_ip]
                self.udp_socket.sendto(("%s -rt %s" % (msg, send_user)).encode("gb2312"), dest_user_ip)
            # 新用户注册
            elif info_list[-2] == '-n':
                password = info_list[-1]
                username = info_list[-3]
                # 验证用户名是否已经存在
                for user in self.users:
                    if username == user.username:
                        data_info = utils.add_log("用户名已经存在！")
                        self.log_text.write(data_info)
                        self.udp_socket.sendto("-rn 注册失败！用户名已经存在".encode("gb2312"), dest_ip)
                        return

                newuser = User.User()
                newuser.set_username(username)
                newuser.set_password(password)
                newuser.set_status(0)
                newuser.set_friend([])
                newuser.set_group([])

                self.users.append(newuser)
                utils.save_user(self.users)

                data_info = utils.add_log("用户 %s 注册成功！" % username)
                self.log_text.write(data_info)
                self.udp_socket.sendto("-rn 注册成功！".encode("gb2312"), dest_ip)
            # 用户登录
            elif info_list[-2] == '-l':
                # 获取用户名和密码
                password = info_list[-1]
                username = info_list[-3]
                # 从持久化文件中读取的用户列表及其信息
                for user in self.users:
                    # 验证密码是否正确
                    if user.username == username and user.password == password:
                        # 登录成功
                        login_info = "登录成功！"
                        # 向客户端发送登陆成功信息
                        self.udp_socket.sendto(("%s -rl %s" % (login_info, username)).encode('gb2312'), dest_ip)

                        # 存储到登录用户列表
                        user_login_dic[username] = dest_ip
                        ip_user_dic[dest_ip] = username
                        user_login_time_dic[username] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                        # 写日志
                        self.log_text.write(utils.add_log("user %s 登录成功！" % username))
                        # 写入服务器登录用户列表
                        self.flush_login_user_list()
                        return
                # 登录失败
                login_info = "用户名或者密码不正确！"
                self.udp_socket.sendto(("%s -rl %s" % (login_info, username)).encode('gb2312'), dest_ip)
                self.log_text.write(utils.add_log("user %s 登录失败！" % username))
            # 返回用户好友列表
            elif info_list[-2] == '-fl':
                friends = self.get_friends(info_list[-1])
                response = "%s -rfl %d" % (' '.join(friends), friends.__len__())
                self.udp_socket.sendto(response.encode("gb2312"), dest_ip)
            # 添加好友
            elif info_list[-2] == '-rmaf':
                # username -rmaf message
                # username: 请求发起者 message: 是否同意
                # 同意则双方成为好友 否则拒绝添加请求
                message = info_list[-1]
                username_req = info_list[-3]
                username_sed = ip_user_dic[dest_ip]
                user_ip = user_login_dic[username_req]
                if message == 'agree':
                    user_req = self.get_user_by_name(username_req)
                    user_sed = self.get_user_by_name(username_sed)

                    user_req.add_friend(user_sed)
                    user_sed.add_friend(user_req)

                    utils.save_user(self.users)
                    req_friends = self.get_friends(username_req)
                    self.udp_socket.sendto(("%s -raf %d %s" % (' '.join(req_friends), req_friends.__len__(), '添加成功！')).encode('gb2312'), user_ip)
                    sed_friends = self.get_friends(username_sed)
                    self.udp_socket.sendto(("%s -raf %d %s" % (' '.join(sed_friends), sed_friends.__len__(), '添加成功！')).encode('gb2312'), dest_ip)
                else:
                    self.udp_socket.sendto('-raf 0 对方拒绝了您的请求'.encode('gb2312'), user_ip)
                pass
            elif info_list[-2] == '-af':
                # 添加好友 -af friend_name
                friend_name = info_list[-1]
                username = ip_user_dic[dest_ip]
                if friend_name not in user_login_dic.keys():
                    self.udp_socket.sendto("-raf 0 对方不在线, 请等待其上线后重试".encode("gb2312"), dest_ip)
                else:
                    friend_ip = user_login_dic[friend_name]
                    self.udp_socket.sendto(("-maf %s" % username).encode("gb2312"), friend_ip)
            # 返回用户群组列表
            elif info_list[-2] == '-gl':
                groups = self.get_groups(info_list[-1])
                response = "%s -rgl %d" % (' '.join(groups), groups.__len__())
                self.udp_socket.sendto(response.encode("gb2312"), dest_ip)
            # 添加群组
            elif info_list[-2] == '-ag':
                '''
                添加群组 username -ag group_name
                规则：
                1. 如果不存在该名称的群组，则直接创建一个新的群组
                2. 如果存在群组，则直接加入该群组，不需要审核
                3. 群组内部的消息所有在线成员都可以直接看到
                4. 不在线人员无法看到历史消息
                '''
                group_name = info_list[-1]
                username = ip_user_dic[dest_ip]
                user = self.get_user_by_name(username)
                group = self.group_exist(group_name)
                if group is not None:
                    # 直接加入该群
                    user.add_group(group)
                else:
                    # 创建一个新群
                    new_group = Group.Group()
                    new_group.set_group_name(group_name)

                    user.add_group(new_group)
                    self.groups.append(new_group)
                utils.save_user(self.users)
                utils.save_group(self.groups)

                self.udp_socket.sendto(("%s -rag success" % username).encode('gb2312'), dest_ip)
                self.flush_groups_list()
            # 群发消息
            elif info_list[-2] == '-tg':
                '''
                格式： msg -tg group_name
                '''
                group_name = info_list[-1]
                username = ip_user_dic[dest_ip]

                users = []
                for g in self.groups:
                    if g.get_group_name() == group_name:
                        users = g.get_users()
                        break

                self.send_to_all(' '.join(info_list[:-2]) + ' %s -rtg %s' % (username, group_name), users)

    def send_to_all(self, msg, users):
        for u in users:
            name = u.get_username()
            if name in user_login_time_dic.keys():
                self.udp_socket.sendto(msg.encode('gb2312'), user_login_dic[name])

    def send_msg(self, event):
        if self.__server_open__:
            event.Skip()
        else:
            self.__server_open__ = False
            self.log_text.write(utils.add_log("服务端关闭中，等待所有用户下线"))
            # self.send_to_all(utils.add_log("服务器系统已关闭，请自行下线"), self.users)
            return

    def stop(self, event):
        self.__server_open__ = False
        self.send_to_all("exit", self.users)
        self.log_text.write(utils.add_log("服务端已关闭，所有用户强制下线！"))
        user_login_dic.clear()
        user_login_time_dic.clear()
        ip_user_dic.clear()
        # self.flush_groups_list()
        self.flush_login_user_list()
        self.send_timer.Stop()
        self.recv_timer.Stop()
        event.Skip()

    def get_friends(self, username):
        friends_name = []
        user = self.get_user_by_name(username)
        friends = user.get_friend()
        for friend in friends:
            friends_name.append(friend.get_username())
        return friends_name

    def get_groups(self, username):
        groups_names = []
        user = self.get_user_by_name(username)
        groups = user.get_group()
        for group in groups:
            groups_names.append(group.get_group_name())
        return groups_names

    def flush_login_user_list(self):
        self.login_user_Grid.ClearGrid()
        index = 0
        for key in user_login_time_dic.keys():
            self.login_user_Grid.SetCellValue(index, 0, key)
            self.login_user_Grid.SetCellValue(index, 1, user_login_time_dic[key])
            index = index + 1
        self.SetStatusText("在线人数：%d" % user_login_dic.keys().__len__(), 0)

    def get_user_by_name(self, username):
        for user in self.users:
            if user.get_username() == username:
                return user

    def group_exist(self,group_name):
        for group in self.groups:
            if group.get_group_name() == group_name:
                return group
        return None

    def flush_groups_list(self):
        self.group_grid.ClearGrid()
        index = 0
        for group in self.groups:
            self.group_grid.SetCellValue(index, 0, group.get_group_name())
            group_usernames = []
            for user in group.get_users():
                group_usernames.append(user.get_username())

            self.group_grid.SetCellValue(index, 1, ','.join(group_usernames))
            index = index + 1