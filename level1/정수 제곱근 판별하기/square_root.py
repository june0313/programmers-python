def nextSqure(n):
    # 함수를 완성하세요
    return int(n ** .5) ** 2 == n and int(n ** .5 + 1) ** 2 or 'no'


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)))
