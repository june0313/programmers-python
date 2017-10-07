def collatz(num):
    count = 0

    while count < 500 and num is not 1:

        if num % 2 is 0:
            num = num // 2
        else:
            num = num * 3 + 1

        count += 1

    return count if count < 500 else -1


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))
print(collatz(4))
print(collatz(99999))
