# 삽입 정렬

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else: # 자신보다 작은 데이터를 만나면 그 위치에서 멈춤
                break
    return array

array = [7, 5, 9, 0, 3, 6, 1, 8, 2, 4]
print(insertion_sort(array))