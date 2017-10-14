def caesar(s, n):
    # answer = []
    #
    # for c in s:
    #     if c.isupper():
    #         answer.append(chr(ord('A') + (ord(c) + n - ord('A')) % 26))
    #     elif c.islower():
    #         answer.append(chr(ord('a') + (ord(c) + n - ord('a')) % 26))
    #     else:
    #         answer.append(c)
    #
    # return answer
    return ''.join([c.isupper() and chr(ord('A') + (ord(c) + n - ord('A')) % 26) or
                    c.islower() and chr(ord('a') + (ord(c) + n - ord('a')) % 26) or
                    c for c in s])


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
