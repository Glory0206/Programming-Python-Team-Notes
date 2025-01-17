# 약수 구하기

# 전체 확인
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# 절반 잘라 확인
def find_divisors_square_root(n):
    divisors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: # n이 4일 경우 2를 2번 넣지 않게 방지
                divisors.append(n // i)
    return sorted(divisors)