def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista

import random

def gerar_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0, 100000))
    return lista

import time

tamanhos = [1000, 5000, 10000, 20000, 50000]

for n in tamanhos:

    lista = gerar_lista(n)

    lista1 = lista.copy()
    lista2 = lista.copy()

    # Insertion Sort
    inicio = time.time()
    insertion_sort(lista1)
    fim = time.time()

    tempo_insertion = fim - inicio

    # Sorted (Timsort)
    inicio = time.time()
    sorted(lista2)
    fim = time.time()

    tempo_sorted = fim - inicio

    print("n =", n)
    print("Insertion Sort:", tempo_insertion)
    print("Sorted (Timsort):", tempo_sorted)
    print()
