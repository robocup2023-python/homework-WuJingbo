'''
题⽬：输⼊某年，判断这⼀年是不是闰年？
程序分析：：判断即可，注意普通闰年和世纪闰年的区别：
1、普通闰年：公历年份是4的倍数的，⼀般是闰年。（如2004年就是闰年）；
2、世纪闰年：公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是世纪闰年，
2000年是世纪闰年）。
'''

n = int(input())
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print("Yes")
else:
    print("No")
