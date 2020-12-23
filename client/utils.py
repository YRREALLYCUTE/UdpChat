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


def add_log(log):
    return add_message(log, "系统")


def add_message(msg, username):
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " %s :\r\n\t %s \r\n" % (username, msg)