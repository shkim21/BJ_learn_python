T = int(input())

for i in range(T):
    a = []
    a = input().split()
    
    if a[1] == '@':
        b = float(a[0]) * 3
    elif a[1] == '%':
        b = float(a[0]) + 5
    elif a[1] == '#':
        b = float(a[0]) - 7

    if len(a) > 2:
        if a[2] == '@':
            b = float(b) * 3
        elif a[2] == '%':
            b = float(b) + 5
        elif a[2] == '#':
            b = float(b) - 7
        
        if len(a) > 3:
            if a[3] == '@':
                b = float(b) * 3
            elif a[3] == '%':
                b = float(b) + 5
            elif a[3] == '#':
                b = float(b) - 7
    print("%0.2f" % b)

    