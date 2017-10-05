def sumMatrix(A, B):
    return [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
