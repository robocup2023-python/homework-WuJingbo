'''
题⽬：将11⽉1⽇的题⽬的解答封装成函数，要求函数接受指定的⾏数等等参数值，为所有函数中的每⼀个变量、所有函数头以及对应的返回值进⾏Type Hint
程序分析：利⽤Python typing标准库
'''
# day7-1

import random
import os


def func() -> None:
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
