def alpha_string46(s):
    # 함수를 완성하세요
    if len(s) is 4 or len(s) is 6:
        for c in s:
            if not ('0' <= c <= '9'):
                return False
        return True
    return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(alpha_string46("a234"))
print(alpha_string46("1234"))
