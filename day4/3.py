m1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        m1[i][j] = int(input())
for i in range(3):
    for j in range(3):
        m2[i][j] = int(input())

for i in range(3):
    for j in range(3):
        print(m1[i][j], end=' ')
    print("\n")

for i in range(3):
    for j in range(3):
        print(m2[i][j], end=' ')
    print("\n")

for i in range(3):
    for j in range(3):
        print(m1[i][j]+m2[i][j], end=' ')
    print("\n")
