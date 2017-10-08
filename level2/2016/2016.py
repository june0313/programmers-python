def getDayName(a, b):
    return ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'][(daysOfPreviousMonths(a) + b + 4) % 7]


def daysOfPreviousMonths(month):
    return sum([daysOfMonth(m) for m in range(1, month)])


def daysOfMonth(month):
    return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month in [4, 6, 9, 11] else 29


# 아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5, 24))
print(getDayName(5, 25))
print(getDayName(5, 26))
print(getDayName(10, 9))
