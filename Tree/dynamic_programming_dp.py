def dp_find_max(triangle):
    height = len(triangle)

    for i in range(1, height):
        for j in range(len(triangle[i])):
            if j == 0: # 가장 왼쪽
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1: # 가장 오른쪽
                triangle[i][j] += triangle[i-1][j-1]
            else: # 가운데
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])       
    return max(triangle[-1])