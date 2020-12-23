import Group
from datetime import datetime


class User:
    def __init__(self):
        self.username = 'user' + datetime.now().strftime("%Y%m%d%H%M%S")
        self.password = '123456'
        self.friend_list = []
        self.group_list = []
        self.status = 0 # 在线状态：1 在线 0 离线

    # get and set 函数
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_friend(self):
        return self.friend_list

    def get_group(self):
        return self.group_list

    def get_status(self):
        return self.status

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_friend(self, friend_list):
        self.friend_list = friend_list

    def set_group(self, group_list):
        self.group_list = group_list

    def set_status(self, status):
        self.status = status

    # 其他函数
    # 添加一个friend
    def add_friend(self, user):
        self.friend_list.append(user)

    # 加入用户组
    def add_group(self, group):
        group.add_user(self)
        self.group_list.append(group)
