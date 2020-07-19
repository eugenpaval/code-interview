def run(n):
    if n <= 3: return n
    a, b, c = 4, 2, 1 
    result = 1
    while n > 3:
        result = a + b + c
        a, b, c = result, a, b
        n -= 1
    
    return          