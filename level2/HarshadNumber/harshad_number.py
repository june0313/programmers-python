def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(i) for i in str(n)]) is 0


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
