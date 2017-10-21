def bestSet(n, s):
    return [s // n] * (n - s % n) + [s // n + 1] * (s % n)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(bestSet(5, 23))
