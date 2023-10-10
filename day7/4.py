'''
题⽬：读取‘test.text’和’copy_test.txt’内容，检查他们的每⼀⾏内容是否相同，输出所有不同的⾏的编号
程序分析：同三
'''
import os


def func(path1, path2):
    with open(path1, 'r') as f1:
        with open(path2, 'r') as f2:
            s1 = f1.readline()
            s2 = f2.readline()
            line = 0
            while s1 or s2:
                line += 1
                if s1 != s2:
                    print(line)
                s1 = f1.readline()
                s2 = f2.readline()


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'test.txt')
copy_file_path = os.path.join(current_dir, 'copy_test.txt')
func(file_path, copy_file_path)
