

def generar_numeros_aleatorios(cantidad):
    import random
    numeros = []
    for i in range(cantidad):
        numeros.append(random.randint(1, 100))
    return numeros

