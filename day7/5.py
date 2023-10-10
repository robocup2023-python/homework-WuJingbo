'''
题⽬：在当前⽬录下新建test⽬录，在test⽬录中⾃建i（i由⽤⼾指定）个以上⽂件，向⽂件中随机输⼊j（j由⽤⼾指定）⾏随机字符，然后遍历该⽬录下的所有⽂件，并在所有⽂件名称和每⼀个⽂件的所有⾏后⾯增加-python 。
程序分析：略
'''
import os
import random
import string


def func(file_path, file_num, line_num):
    for i in range(file_num):
        file_name = f"file{i}.txt"
        file_path = os.path.join(test_dir, file_name)
        with open(file_path, "w") as file:
            for j in range(line_num):
                random_str = "".join(random.choices(
                    string.ascii_letters + string.digits, k=10))
                file.write(f"{random_str}\n")

    for root, dirs, files in os.walk(test_dir):
        for file_name in files:
            new_file_name = file_name.replace(".txt", "-python.txt")
            file_path = os.path.join(root, file_name)
            new_file_path = os.path.join(root, new_file_name)
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(new_file_path, "w") as new_file:
                for line in lines:
                    new_file.write(f"{line.strip()}-python\n")


current_dir = os.path.dirname(os.path.abspath(__file__))
test_dir = os.path.join(current_dir, "test")
os.makedirs(test_dir, exist_ok=True)

file_num = int(input("请输入要创建的文件数量："))
line_num = int(input("请输入每个文件要创建的行数："))

func(test_dir, file_num, line_num)
