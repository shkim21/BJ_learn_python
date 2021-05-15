M, N = map(int, input().split())

if M >= N:
    a = N-1 + (M-1)*N
else:
    a = M-1 + (N-1)*M

print(a)