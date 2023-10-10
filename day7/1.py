'''
题⽬： ⾃⾏制作⼀个10⾏3列⽂件，每列内容为随机数，以逗号作为分割符，写程序输出第⼆列的最⼤值，最⼩值，平均值，中位数
程序分析：随机数的⽣成有random标准库。
'''
import random
import os


def func():
    data = [[random.randint(0, 100) for j in range(3)] for i in range(10)]
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data1.txt')

    with open(file_path, 'w') as f:
        for row in data:
            line = ','.join(map(str, row))
            f.write(line + '\n')

    second_column = [row[1] for row in data]
    print(f"max_value:{max(second_column)}")
    print(f"min_value:{min(second_column)}")
    print(f"average_value:{sum(second_column)/10}")
    print(
        f"median_value:{(sorted(second_column)[4]+sorted(second_column)[5])/2}")


func()
