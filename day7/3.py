'''
题⽬：读取上述test.txt的⽂件内容，分别在⽂件的开头和结尾处追加字符串python
程序分析：查询Python⽂件对象⽀持的⽅法，例如有如seek、tell等等；参考Python语⾔及其运⽤
'''
import os


def func(path):
    with open(file_path, "r+") as file:
        file.seek(0)
        content = file.read()
        file.seek(0)
        file.write("python" + content)
        file.seek(0, 2)
        file.write("python")


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'test.txt')
func(file_path)
