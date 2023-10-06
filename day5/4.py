'''
题⽬：在当前.py⽂件⽬录新建⽬录img, ⾥⾯包含100个⽂件, 100个⽂件名各不相同(X4G5.png)
程序分析：Python的pathlib库和Python的os库都提供了⽂件路径相关的函数和类
'''
import os


def create():
    os.mkdir("./img")
    for i in range(1, 101):
        filename = f"{i}.png"
        with open(f"./img/{filename}", "w"):
            pass


create()
