# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 19:21
# @Author  : huyulan
# @Email   : huyulan@boe.com.cn
# @File    : ReadFile.py
# @Software: PyCharm
# ssh连接

import paramiko


def server_connect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 加上这句话不用担心选yes的问题，会自动选上（用ssh连接远程主机时，第一次连接时会提示是否继续进行远程连接，选择yes）
    ssh.connect(hostname='10.12.11.9', port=22, username='root', password='root')

    return ssh


if __name__ == '__main__':
    ssh = server_connect()
    sftp_client = ssh.open_sftp()
    file_path = "/home/yulan/program/gensim-similarity/data/document.txt"
    remote_file = sftp_client.open(file_path)
    try:
        for line in remote_file:
            print(line, end='')
    finally:
        remote_file.close()

