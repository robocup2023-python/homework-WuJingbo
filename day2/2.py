a = int(input("please enter the number: "))
n = int(input("please enter the times: "))
sum = 0

for i in range(1,n+1):
    tmp = a
    for j in range(1,i+1):
        sum += tmp
        tmp *= 10

print(sum)