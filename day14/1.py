import pandas as pd
import threading
import multiprocessing
import time
import os
import re
import csv
from tqdm import tqdm

dic = {}


def recoder(dic):
    def timer(func):
        def wrapper(*args, **kwargs):
            st = time.time()
            result = func(*args, **kwargs)
            et = time.time()
            print(
                f"pid为{os.getpid()} 线程id为{threading.get_ident()}的函数读取文件{args[0]}的单词数为{result}，运行时长{round(et-st,5)}")
            dic[args[0]] = result
            return result
        return wrapper
    return timer


@recoder(dic)
def count_word(path):
    res = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            res += len(re.findall(' ', line))+1
    return res


def read_files(path):
    thread_list = []
    global dic
    for file in os.listdir(path):
        newfile = path + '/' + file
        new_thread = threading.Thread(target=count_word, args=(newfile,))
        thread_list.append(new_thread)
        new_thread.start()
    for thread in thread_list:
        thread.join()
    return dic


def main(path):
    global dic
    pool = multiprocessing.Pool()
    result_list = []
    second_dir = []
    for file in os.listdir(path):
        newfile = path+'/'+file
        if os.path.isdir(newfile):
            second_dir.append(newfile)
        else:
            new_thread = threading.Thread(target=count_word, args=(newfile,))
            new_thread.start()

    for dir in second_dir:
        for file in os.listdir(dir):
            newfile = dir + '/' + file
            result_list.append(pool.apply_async(read_files, args=(newfile,)))
    pool.close()
    pool.join()
    for res in result_list:
        dic.update(res.get())
    return dic


if __name__ == '__main__':
    dic.clear()
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'download')
    main(path)
    series = pd.Series(dic)
    result_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'result.csv')
    series.to_csv(result_path)
