# 떡볶이 떡 만들기
n, m = map(int, input().split())
cm_list = list(map(int, input().split()))

start = 0
finish = max(cm_list)

while start <= finish:
    h = (start + finish) // 2

    total = sum(max(0, x-h) for x in cm_list)

    if total < m:
        finish = h - 1
    else:
        result = h
        start = h + 1

print(result)
