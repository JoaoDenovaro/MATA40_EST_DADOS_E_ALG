def div(num1, num2):
    '''Insere como entrada 2 inteiros e retorna divisão do 1º pelo 2º'''
    cont = 0
    while num1 != 0:
        num1 -= num2
        cont += 1
    return cont

print(f'A divisão é {div(12,6)}')