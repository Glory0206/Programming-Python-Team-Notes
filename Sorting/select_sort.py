# 선택 정렬

def select_sort(array):
    for i in range(len(array)):
        min_index = i
        
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

array = [7, 5, 9, 0, 3, 6, 1, 8, 2, 4]
print(select_sort(array))