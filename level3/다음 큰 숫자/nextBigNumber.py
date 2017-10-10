def nextBigNumber(n):
    next_number = n + 1

    while bin(n).count('1') != bin(next_number).count('1'):
        next_number += 1

    return next_number


# 아래 코드는 테스트를 위한 출력 코드입니다.
print(nextBigNumber(78))
