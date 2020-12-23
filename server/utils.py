from datetime import datetime
import pickle
import os
from datetime import datetime
from Crypto.Cipher import DES


KEY = b'12345678'
des = DES.new(KEY, DES.MODE_ECB)


def pad(text):
    """
    # 加密函数，如果text不是8的倍数【加密文本text必须为8的倍数！】，那就补足为8的倍数
    :param text:
    :return:
    """
    while len(text.encode('gb2312')) % 8 != 0:
        text += ' '
    return text


def encrypt_msg(msg):
    """
    加密函数，使用DES算法
    :param msg: 加密的信息
    :return: 加密后的文本
    """
    padded_text = pad(msg)
    encrypt_text = des.encrypt(padded_text.encode('gb2312'))
    return encrypt_text


def decrypt_msg(decrypt_text):
    plain_text = des.decrypt(decrypt_text).decode('gb2312').rstrip(' ')
    return plain_text


def save_user(user_list):
    with open('users', 'wb') as f:
        pickle.dump(user_list, f)


def save_group(group_list):
    with open('groups', 'wb') as f:
        pickle.dump(group_list, f)


def get_user():
    with open('users', 'rb') as f:
        if os.stat('users').st_size == 0:
            return []
        user_list = pickle.load(f)
    return user_list


def get_group():
    with open('groups', 'rb') as f:
        if os.stat('groups').st_size == 0:
            return []
        group_list = pickle.load(f)
    return group_list


def add_log(log):
    return add_message(log, "系统")


def add_message(msg, username):
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " %s :\r\n\t %s \r\n" % (username, msg)