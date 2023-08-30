def inteiros(num):
    '''Recebe um número inteiro positivo x e retorne a soma de todos os inteiros positivos entre 1 e x'''
    if num <= 0:
        return 'O número tem que ser positivo'
    
    return sum(range(2, num))

print(inteiros(8))