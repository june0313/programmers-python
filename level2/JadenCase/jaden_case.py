def Jaden_Case(s):
    # 함수를 완성하세요
    # return ' '.join(map(lambda w: w[0].upper() + w[1:].lower(), s.split()))
    return ' '.join([w[0].upper() + w[1:].lower() for w in s.split()])


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
