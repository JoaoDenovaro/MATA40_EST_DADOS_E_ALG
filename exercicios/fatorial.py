def fatorial(num):
    for i in range (1, num):
        num *= i
    return num

print(fatorial(10))