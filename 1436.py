N = int(input())

end_numbers= []
for i in range(5000000):
    if '666' in str(i):
        end_numbers.append(i)
# print(len(a))

print(end_numbers[N-1])