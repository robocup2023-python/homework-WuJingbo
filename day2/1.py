string = input()
alpha = digit = space = other = 0
for i in range(0,len(string)):
    ch = string[i]
    if ch.isalpha():
        alpha += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
    else:
        other += 1
print(f"alpha:{alpha}")
print(f"digit:{digit}")
print(f"space:{space}")
print(f"other:{other}")