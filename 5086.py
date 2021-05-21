T = True

while T:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        T = False
        continue
    
    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")