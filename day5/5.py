'''
题⽬：在上⼀题的基础上，随机将50个⽂件改名为.jpg结尾
程序分析：善⽤搜索引擎
'''
import random
import os


def rename(path):
    random_numbers = random.sample(range(1, 101), 50)
    for number in random_numbers:
        old_name = f'{path}/{number}.png'
        new_name = f'{path}/{number}.jpg'
        os.rename(old_name, new_name)


rename('./img')
