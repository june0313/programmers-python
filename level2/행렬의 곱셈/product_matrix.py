def productMatrix(A, B):
    return [[(sum([A[i][k] * B[k][j] for k in range(len(A[i]))])) for j in range(len(B[0]))] for i in range(len(A))]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [[1, 2], [2, 3]]
b = [[3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a, b)))
