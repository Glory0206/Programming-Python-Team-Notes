# 계수 정렬

def counting(array):
    count = [0] * (max(array) + 1)

    for i in array:
        count[i] += 1

    for i in range(len(count)):
        for _ in range(count[i]):
            print(i, end=' ')

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
counting(array)