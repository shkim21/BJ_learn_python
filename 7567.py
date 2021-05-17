plate = str(input())

N = len(plate)

P = int(N)* 10

for i in range(N-1):
    if plate[i] == plate[i+1]:
        P -= 5

print(P)
