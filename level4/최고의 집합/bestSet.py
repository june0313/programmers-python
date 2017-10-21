from functools import reduce


def bestSet(n, s):
    return findBestSet(n, s, s, [])


def findBestSet(n, s, remain, set):
    if n == 1:
        return set + [remain]

    best_set = []
    for i in range(1, s):

        if remain - i == 0:
            break

        a_set = findBestSet(n - 1, s, remain - i, set + [i])

        if len(best_set) == 0:
            best_set = a_set
        elif len(a_set) != 0 and reduce(lambda a, b: a * b, a_set) >= reduce(lambda a, b: a * b, best_set):
            best_set = a_set

    return sorted(best_set)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(bestSet(5, 23))
