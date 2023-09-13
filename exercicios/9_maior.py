import numpy as np

def maior(vet):
    vet = sorted(vet)
    return vet[-1]

teste = np.array([0, 5, 10, 3])

print(maior(teste))