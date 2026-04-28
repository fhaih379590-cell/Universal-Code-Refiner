# 这是一段劣质代码：变量命名模糊，有硬编码，逻辑混乱
import os

def check():
    ip = "192.168.1.105" # 硬编码IP
    key = "secret_password_123" # 敏感信息
    list = [1,2,3,4,5]
    for i in list:
        if i % 2 == 0:
            print("even")
        else:
            print("odd")
    return True

check() 
