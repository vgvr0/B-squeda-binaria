def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        elemento_medio = lista[medio]

        if elemento_medio == objetivo:
            return medio
        elif elemento_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

# Ejemplo de uso
numeros = [2, 4, 7, 10, 14, 19, 22, 25, 30]
objetivo = 19

indice = busqueda_binaria(numeros, objetivo)

if indice != -1:
    print("El objetivo", objetivo, "se encuentra en el índice", indice)
else:
    print("El objetivo", objetivo, "no se encontró en la lista.")
