def jumpCase(num):
    return num < 3 and num or jumpCase(num - 1) + jumpCase(num - 2)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(5))
