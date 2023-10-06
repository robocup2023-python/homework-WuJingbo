ans = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and i!=k and j!=k):
                ans += 1
                print(100*i + 10*j + k)
print(ans)