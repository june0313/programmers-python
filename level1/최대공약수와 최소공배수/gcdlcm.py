def gcdlcm(a, b):
    return [gcd(a, b), lcm(a, b)]


def lcm(a, b):
    return a * b / gcd(a, b)


def gcd(a, b):
    if a > b:
        a, b = b, a

    if (b % a) is 0:
        return a

    return gcd(b % a, a)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3, 12))
