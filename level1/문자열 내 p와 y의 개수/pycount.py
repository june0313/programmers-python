def numPY(s):
    # 함수를 완성하세요
    count = 0

    for c in s:
        if c.lower() == 'p':
            count += 1

        if c.lower() == 'y':
            count -= 1

    return count is 0


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numPY("pPoooyY"))
print(numPY("Pyy"))
