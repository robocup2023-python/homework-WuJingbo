import random
import os
import time


class Universe:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.world = [[' ' for _ in range(width)] for _ in range(height)]

    def show(self):
        print('\033[H', end='')  # 清空屏幕当前输出
        for row in self.world:
            print(''.join(row))
        time.sleep(0.2)  # 每秒5次迭代

    def seed(self):
        for i in range(self.height):
            for j in range(self.width):
                if random.random() < 0.25:  # 约25%的细胞激活
                    self.world[i][j] = '*'

    def alive(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False  # 边界情况处理
        return self.world[y][x] == '*'

    def neighbors(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.alive(x+j, y+i):
                    count += 1
        return count

    def next(self):
        new_world = [[' ' for _ in range(self.width)]
                     for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                alive = self.alive(j, i)
                count = self.neighbors(j, i)
                if alive and (count < 2 or count > 3):
                    new_world[i][j] = ' '  # 存活细胞少于2个或多于3个则死亡
                elif not alive and count == 3:
                    new_world[i][j] = '*'  # 死细胞邻近有3个存活细胞则存活
                else:
                    new_world[i][j] = self.world[i][j]
        self.world = new_world

    def step(self, steps):
        for _ in range(steps):
            self.show()
            self.next()


if __name__ == '__main__':
    width = 80
    height = 15
    universe = Universe(width, height)
    universe.seed()
    universe.step(100)
