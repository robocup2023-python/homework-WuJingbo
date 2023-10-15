import os
import random
import string
import threading


def create_files(file_path, file_num, line_num):
    for i in range(file_num):
        file_name = f"file{i}.txt"
        file_path = os.path.join(test_dir, file_name)
        with open(file_path, "w") as file:
            for j in range(line_num):
                random_str = "".join(random.choices(
                    string.ascii_letters + string.digits, k=10))
                file.write(f"{random_str}\n")


def rename_files():
    files = os.listdir(test_dir)
    for file_name in files:
        if file_name.endswith(".txt"):
            new_file_name = file_name.replace(".txt", "-python.txt")
            old_file_path = os.path.join(test_dir, file_name)
            new_file_path = os.path.join(test_dir, new_file_name)
            os.rename(old_file_path, new_file_path)


current_dir = os.path.dirname(os.path.abspath(__file__))
test_dir = os.path.join(current_dir, "test")
os.makedirs(test_dir, exist_ok=True)

file_num = int(input("请输入要创建的文件数量："))
line_num = int(input("请输入每个文件要创建的行数："))

create_thread = threading.Thread(
    target=create_files, args=(test_dir, file_num, line_num))
rename_thread = threading.Thread(target=rename_files)

create_thread.start()
rename_thread.start()

create_thread.join()
rename_thread.join()
