import csv
import os
import pandas as pd


def create(path, data):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def func(path):
    df = pd.read_csv(path)
    print(df)
    df.drop('c3', axis=1, inplace=True)
    df['c1'] += df['c2']
    print(df)


current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, 'test.csv')
data = [
    ['c1', 'c2', 'c3'],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

create(path, data)
func(path)
