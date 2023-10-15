import argparse
import csv
import os
import pandas as pd


def create(path, data):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def func(path, number):
    df = pd.read_csv(path)
    print(df)
    columns = list(df.columns)
    column_to_drop = columns[number]
    df.drop(column_to_drop, axis=1, inplace=True)
    df['c1'] += df['c2']
    print(df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="文件路径")
    parser.add_argument("--number", type=int, help="要删除的列索引")
    args = parser.parse_args()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, args.path)
    data = [
        ['c1', 'c2', 'c3'],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    create(path, data)
    func(path, args.number)

# python 2.py --path test.csv --number 2
