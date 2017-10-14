def noOvertime(n, works):
    # 야근 지수를 최소화 하였을 때의 야근 지수는 몇일까요?
    for i in range(n):
        works[works.index(max(works))] = max(max(works) - 1, 0)
    return sum([w ** 2 for w in works])


print(noOvertime(4, [4, 3, 3]))
print(noOvertime(45, [5, 14, 6, 7, 6]))
