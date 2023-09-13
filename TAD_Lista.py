import numpy as np

class Lista:
    def __init__(self, qt_elementos):
        self.max = qt_elementos
        self.tam = 0
        self.elems = np.zeros(self.max)
        return print(f'Vetor criado: {self.elems}')
    
    def imprimir(self):
        return print(f'Vetor: {self.elems}')

    def setMax(self, novo_max):
        self.max = novo_max

        if novo_max <= len(self.elems):
            self.elems = self.elems[:novo_max]
            self.tam = self.max
            print(f'O novo max é {self.max}')
            return self.imprimir()
        
        else:
            temp = self.elems
            self.elems = np.zeros(self.max)
            
            for i in range(len(temp)):
                self.elems[i] = temp[i]

            print(f'O novo max é {self.max}')
            return self.imprimir()
    
    def isEmpty(self):
        if self.tam == 0:
            return print('Lista vazia')
        else: 
            return print('Há elementos na lista')
    
    def inserir(self, elem):
        if self.tam == self.max:
            return print('Erro, lista cheia')
        
        else:
            self.elems[self.tam] = elem
            self.tam += 1
            print(f'Elemento {elem} adicionado')
            return self.imprimir()

    def limpar(self):
        self.tam = 0
        self.elems = np.zeros(self.max)
        print('Lista limpa')
        return self.imprimir()

def main():
    l = Lista(4)
    l.inserir(5)
    l.inserir(1)
    l.inserir(6)
    l.inserir(3)
    l.isEmpty()
    l.imprimir()
    l.setMax(2)
    l.setMax(10)
    l.limpar()
    l.isEmpty()
    l.setMax(2)


if __name__ == '__main__':
    main()