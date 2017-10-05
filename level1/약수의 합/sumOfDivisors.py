def sumDivisor(num):
    return sum([n for n in range(1, num + 1) if num % n is 0])


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))
