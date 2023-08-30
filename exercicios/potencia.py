def pot(num1, num2):
    '''Insere como entrada 2 inteiros e retorna potência do 1º pelo 2º'''
    num1 = int(num1)
    temp = num1
    num2 = int(num2)
    for i in range(1, num2):
        num1 *= temp
    return num1

print(pot(2,8))