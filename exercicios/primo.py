def primo(num):
    '''Recebe um número e retorna 1 se for primo, 0 se não for primo'''
    for i in range(2,num):
        if num % i == 0:
            return 0
        
    return 1

print(primo(14))