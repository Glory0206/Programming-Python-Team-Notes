n = 7
data = [7, 5, 1, 2, 8, 13, 11]

def quick_sort(data, start, end): # start와 end는 index
    if start >= end: # 부분배열의 크기가 1이라면, 함수 종료
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and data[left] <= data[pivot]: # 확인하는 숫자가 pivot보다 작다면, 이동 없이 index 증가
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right: # 양쪽에서 pivot과의 값을 확인하다 index가 만나 넘게되면
            data[right], data[pivot] = data[pivot], data[right]
        else: # 아직 index가 만나기 이전 left index 내의 값은 pivot보다 크고, right index 내의 값은 pivot보다 작을 때 값 교환
            data[left], data[right] = data[right], data[left]

        quick_sort(data, start, right - 1) # pivot 기준 좌측 리스트들을 상대로 정렬
        quick_sort(data, right + 1, end) # pivot 기준 우측 리스트들을 상대로 정렬

    return data

result_data = quick_sort(data, 0, n-1)

print(f"quick_sort: {result_data}")
