def expressions(num):
    count = 0
    for i in range(1, num + 1):
        acc = 0
        for j in range(i, num + 1):
            acc += j
            if acc > num:
                break
            if acc == num:
                count += 1
                break
    return count


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15))
