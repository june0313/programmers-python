def water_melon(n):
    # 함수를 완성하세요.
    return ''.join(['수' if i % 2 is 0 else '박' for i in range(0, n)])


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3))
print("n이 4인 경우: " + water_melon(4))
