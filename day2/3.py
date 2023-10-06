ans = 100
maxHeight = 100
times = 1

while times <= 10:
    print(f"{times}:{ans},{maxHeight}")
    ans += maxHeight
    maxHeight *= 0.5
    times += 1

