'''
题⽬：输⼊某年某⽉某⽇，判断这⼀天是这⼀年的第⼏天？
程序分析：以3⽉5⽇为例，应该先把前两个⽉的加起来，然后再加上5天即本年的第⼏天。注意闰年的特殊情况
'''

year = int(input("please enter the year:"))
month = int(input("please enter the month:"))
day = int(input("please enter the day:"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    array = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    array = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

ans = 0
for i in range(0, month-1):
    ans += array[i]
print(ans+day)
