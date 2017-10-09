def numberOfPrime(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    return len(list(filter(isPrime, range(1, n + 1))))


def isPrime(n):
    return list(filter(lambda i: n % i is 0, range(1, n + 1))) == [1, n]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(10))
print(numberOfPrime(5))
