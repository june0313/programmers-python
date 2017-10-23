def chooseCity(n, cities):
    answer = 0
    min_distance = 0

    for i in range(n):
        city_number = cities[i][0]
        distance = sum([abs(city[0] - city_number) * city[1] for city in cities if city[0] != city_number])

        if min_distance == 0 or distance < min_distance:
            answer = city_number
            min_distance = distance

    return answer


# 아래 코드는 출력을 위한 테스트 코드입니다.
print(chooseCity(3, [[1, 5], [2, 2], [3, 3]]))
