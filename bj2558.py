a = int(input())
b = int(input())

first = b//100
second = b//10 - first*10
third = b%10
print(a*third)
print(a*second)
print(a*first)
print(a*first*100+a*second*10+a*third)