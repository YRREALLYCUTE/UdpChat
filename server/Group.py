from _datetime import datetime


class Group:

    def __init__(self):
        self.users = []
        self.group_name = 'group' + datetime.now().strftime("%Y%m%d%H%M%S")

    def get_users(self):
        return self.users

    def get_group_name(self):
        return self.group_name

    def set_users(self, users):
        self.users = users

    def set_group_name(self, group_name):
        self.group_name = group_name

    # 向group中添加一个user
    def add_user(self, user):
        self.users.append(user)

    def del_user(self, user):
        self.users.remove(user)