def fibonacci_top_down(n):
    fibonacci = [0] * 100

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    if fibonacci[n] != 0:
        return fibonacci[n]
    
    fibonacci[n] = fibonacci_top_down(n-1) + fibonacci_top_down(n-2)
    return fibonacci[n]

print(fibonacci_top_down(4))

def fibonacci_bottom_up(n):
    fibonacci = [0, 1]

    if n == 0:
        return 0

    for i in range(2, n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    return fibonacci[n]
