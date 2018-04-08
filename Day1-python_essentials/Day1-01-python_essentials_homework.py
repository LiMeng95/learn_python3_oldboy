# -*- coding: utf-8 -*-
# Python: 3.6
# Author: Meng Li
# 2018/03/11  涉及简单交互，split函数字符串处理，简单文件读写

file_of_name_password = open("NameAndPasswd.txt", 'r')
file_of_locked_name = open("LockedName.txt", 'r+')
file_of_name_password.buffer
username_input = input("Plz input your username:")
password_input = input("Plz input your password:")

# 首先判断用户名是否被锁定
Locked = 0  # 0表示未锁定，1表示锁定
while Locked == 0:
    locked_name = file_of_locked_name.readline().split()  # 获取被锁定账号名称,split可去除'\n\t\r'空格等
    if locked_name:  # 如果没有到文件结尾
        if locked_name[0] == username_input:
            print("Username %s has been locked!" % username_input)
            Locked = 1
    else:  # 如果已到文件结尾
        break

# 如未锁定，则开始登陆
Login_succeed = 0  # 0表示未成功登陆，1表示成功登录
while Locked == 0 and Login_succeed == 0:
    username = file_of_name_password.readline().split()  # 按顺序读取已保存的用户名
    if username:  # 如果没有到文件结尾
        password = file_of_name_password.readline().split()[0]  # 按顺序读取已保存的密码
        if username_input == username[0]:  # 如果用户名匹配
            for password_input_count in range(3):
                if password_input == password:  # 如果密码匹配
                    print("Welcome user %s login..." % username_input)
                    Login_succeed = 1
                    break
                else:  # 重新输入密码
                    print("Wrong password, Input again. You have %d chances remain." % (2-password_input_count))
                    if password_input_count < 2:
                        password_input = input("Plz input your password:")
                    else:  # 输入三次未成功
                        file_of_locked_name.write(username_input)
                        file_of_locked_name.write('\n')
                        print("Try to many times. Username %s has been locked!" % username_input)
                        Locked = 1
    else:  # 如果已到文件结尾
        print("Username %s do not exist." % username_input)
        break

file_of_name_password.close()
file_of_locked_name.close()
