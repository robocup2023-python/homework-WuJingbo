'''
题⽬：遍历上述⽂件⽬录下的所有⽂件，写程序判断⽂件名字和内容⾥是否含有python ，如果含有，则将python 替换为class 。
'''

import os


def replace_python_with_class(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, "r") as file:
                lines = file.readlines()
            content_changed = False
            new_lines = []
            for line in lines:
                if "python" in line:
                    line = line.replace("python", "class")
                    content_changed = True
                new_lines.append(line)
            if content_changed:
                with open(file_path, "w") as new_file:
                    new_file.writelines(new_lines)
            if "python" in file_name:
                new_file_name = file_name.replace("python", "class")
                new_file_path = os.path.join(root, new_file_name)
                os.rename(file_path, new_file_path)


current_dir = os.path.dirname(os.path.abspath(__file__))
test_dir = os.path.join(current_dir, "test")
replace_python_with_class(test_dir)
