'''
题⽬：在⼯作⽬录下写程序创建⼀个⽂件（ test.txt ）并随机⽣成i（i由⽤⼾指定）⾏内容（包含ASCII标准的任意⾮控制字符）。写程序实现该⽂件的拷⻉，拷⻉⽂件⽂件命名为copy_test.txt 。
程序分析：同上，随机使⽤random模块；ASCII标准字符是什么则需要利⽤搜索引擎；参考Python语⾔及其运⽤
'''

import random
import os


def generate_random_content(num_lines):
    lines = []
    for _ in range(num_lines):
        line = ''.join(chr(random.randint(33, 126))
                       for _ in range(random.randint(10, 50)))
        lines.append(line)
    return '\n'.join(lines)


def create_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def copy_file(original_file_path, copy_file_path):
    with open(original_file_path, 'r') as original_file:
        content = original_file.read()

    create_file(copy_file_path, content)


num_lines = int(input("请输入要生成的行数："))
content = generate_random_content(num_lines)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'test.txt')
copy_file_path = os.path.join(current_dir, 'copy_test.txt')
create_file(file_path, content)
copy_file(file_path, copy_file_path)
