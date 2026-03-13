import sys
import time

sys.setrecursionlimit(2500)

def fatorial(numero: int) -> int:
    """Calcula o fatorial de forma recursiva."""
    if numero == 0:
        return 1
    return numero * fatorial(numero - 1)

# Análise de Complexidade:
# O algoritmo de fatorial recursivo realiza uma chamada recursiva para cada valor
# de n até chegar ao caso base (n = 0). Dessa forma, o número de operações cresce
# proporcionalmente ao valor de entrada. Portanto, a complexidade de tempo do
# algoritmo é O(n). Além disso, como cada chamada recursiva é armazenada na pilha
# de execução até que o caso base seja alcançado, o consumo de memória também
# cresce linearmente, resultando em complexidade de espaço O(n).

""" Valores """
experimentos = [10, 100, 500, 1000]
resultados = {}

for valor in experimentos:
    marca_inicial = time.perf_counter()

    fatorial(valor)

    marca_final = time.perf_counter()

    duracao = marca_final - marca_inicial
    resultados[valor] = duracao

    print(f"Processado: n={valor:4} | Delta T: {duracao:.8f}s")