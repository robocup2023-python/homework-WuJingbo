'''
题⽬：创建⽂件data.txt,⽂件共100000⾏，每⾏存放⼀个随机的1〜100之间的整数
程序分析：random库
'''
import random

file = open("data.txt", "w")

for i in range(100000):
    num = random.randint(1, 100)
    file.write(str(num) + "\n")

file.close()
