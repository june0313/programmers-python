from functools import reduce


def gcd(a, b): return a if (b % a == 0) else gcd(b % a, a)


def lcm(a, b): return a * b / gcd(a, b)


def nlcm(num): return reduce(lcm, sorted(num), 1)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2, 6, 8, 14]))
