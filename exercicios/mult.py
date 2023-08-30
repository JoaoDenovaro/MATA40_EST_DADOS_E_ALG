def mult(num1, num2):
    '''Insere como entrada 2 inteiros e retorna multiplicação entre eles'''
    num1 = int(num1)
    temp = num1
    num2 = int(num2)
    for i in range(1, num2):
        num1 += temp
    return num1

print(mult(2,6))