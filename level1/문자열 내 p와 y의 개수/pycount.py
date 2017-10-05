def numPY(s):
    # 함수를 완성하세요
    p_count = 0
    y_count = 0

    for c in s:
        if c.lower() == 'p':
            p_count += 1

        if c.lower() == 'y':
            y_count += 1

    return p_count == y_count


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numPY("pPoooyY"))
print(numPY("Pyy"))
