def chooseCity(n, city):
    cities = sorted(city, key=lambda c: c[0])

    l_population, r_population, l_distance, r_distance = 0, 0, [0], [0]

    for i in range(n):
        l_idx, r_idx = i,  -(i + 1)

        if l_idx > 0:
            l_population += cities[l_idx - 1][1]
            l_distance.append(l_distance[l_idx - 1] + l_population * (cities[l_idx][0] - cities[l_idx - 1][0]))

        if r_idx < -1:
            r_population += cities[r_idx + 1][1]
            r_distance.insert(0, r_distance[r_idx + 1] + r_population * (cities[r_idx + 1][0] - cities[r_idx][0]))

    shortest_distance = 0
    answer = cities[0][0]

    for i in range(n):
        total_distance = l_distance[i] + r_distance[i]

        if shortest_distance == 0:
            shortest_distance = total_distance
        elif shortest_distance > total_distance:
            shortest_distance = total_distance
            answer = cities[i][0]

    return answer


# 아래 코드는 출력을 위한 테스트 코드입니다.
print(chooseCity(3, [[1, 5], [2, 2], [3, 3]]))
