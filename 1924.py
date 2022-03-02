x, y = map(int, input().split())

yoil = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#1월 : 31일


def calculate():
    dayss = 0
    if x > 1:
        for i in range(1, x):
            dayss += days[i-1]
    dayss += y

    # print("dayss:", dayss)
    # print("dayss div 7:", dayss%7)
    print(yoil[dayss%7])

calculate()