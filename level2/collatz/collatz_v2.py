def collatz(num):
    for i in range(500):
        if num is 1:
            return i

        num = num % 2 is 0 and num // 2 or num * 3 + 1

    return -1


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))
print(collatz(4))
print(collatz(1))
print(collatz(99999))
