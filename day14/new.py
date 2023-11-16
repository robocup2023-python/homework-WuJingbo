import pandas as pd
import multiprocessing
import os
import re
import timeit
from collections import Counter


def get_word_count(filepath):
    with open(filepath, encoding="UTF-8") as file:
        content = file.read()
        content = re.sub(r"\W", " ", content)
        word_count = Counter(content.split())
    return word_count


def process_files(filespath, filenames):
    pool = multiprocessing.Pool(processes=10)
    results = []
    for name in filenames:
        filepath = os.path.join(filespath, name)
        result = pool.apply_async(get_word_count, (filepath,))
        results.append(result)
    pool.close()
    pool.join()

    thread_word_count = Counter()
    for result in results:
        word_count = result.get()
        thread_word_count += word_count

    return thread_word_count


def main():
    total_word_count = Counter()
    manager = multiprocessing.Manager()
    dir_names = os.listdir(filesloc)
    for dir_name in dir_names:
        if os.path.isdir(os.path.join(filesloc, dir_name)):
            filenames = os.listdir(os.path.join(filesloc, dir_name))
            process_filenames = manager.list(filenames)
            process = multiprocessing.Process(
                target=process_files, args=(os.path.join(filesloc, dir_name), process_filenames))
            process.start()
            process.join()
            thread_word_count = Counter()
            for filename in process_filenames:
                filepath = os.path.join(filesloc, dir_name, filename)
                word_count = get_word_count(filepath)
                thread_word_count += word_count
            total_word_count += thread_word_count

    word_count_df = pd.DataFrame(
        list(total_word_count.items()), columns=["word", "count"])
    word_count_df.to_csv("./output.csv", index=None)


if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "download")
    filesloc = data_path + "/Texts"
    cnt_time = timeit.Timer("main()", "from __main__ import main")
    print("程序运行时间：", cnt_time.timeit(number=1), "秒")
