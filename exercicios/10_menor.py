import numpy as np

def menor(vet):
    vet = sorted(vet)
    return vet[0]

teste = np.array([0, 5, 10, 3])

print(menor(teste))