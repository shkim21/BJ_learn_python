import math

A, B, V = map(int, input().split())

print(math.ceil((V-A)/(A-B))+1)

###시간 초과,,,
# day = 0
# today_height = 0

# while today_height < V:
#     day += 1
#     today_height += A
#     if today_height >= V:
#         break
#     today_height -= B

# print(day)


#print(V-A+1)