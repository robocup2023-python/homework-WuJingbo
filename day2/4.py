for i in range(100,1000):
    # print(i,pow(i%10,3) + pow(int((i/10))%10,3) + pow(int(i/100),3))
    if pow(i%10,3) + pow(int((i/10))%10,3) + pow(int(i/100),3) == i:
        print(i)