def no_continuous(s):
    result = []

    for c in s:
        if len(result) is 0 or result[-1] is not c:
            result.append(c)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(no_continuous("133303"))
