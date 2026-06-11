# Problema da Soma de Subconjuntos (Subset Sum Problem)
# 
# Classe do Problema: NP-Completo
# A verificação de uma resposta pronta (dado um subconjunto, verificar se a soma é T) é rápida e feita em Tempo Polinomial O(n).
# No entanto, encontrar a solução do zero exige que o algoritmo explore um espaço de busca com complexidade exponencial no pior caso.
# 
# Complexidade de Tempo: O(2^n) no pior caso (Força Bruta / Backtracking simples).
# Onde 'n' é o número de elementos no conjunto S. Para n=30, são 2^30 (aprox. 1.07 bilhão) de combinações.

import itertools
import random
import time

def subset_sum_backtracking(S, T):
    """
    Encontra um subconjunto de S cuja soma seja exatamente T usando Backtracking.
    Retorna o subconjunto se encontrado, ou None caso não exista.
    """
    n = len(S)
    
    # Função interna recursiva para explorar os ramos (com ou sem o elemento atual)
    def backtrack(index, current_sum, path):
        # Condição de sucesso: soma atingida e subconjunto não vazio
        if current_sum == T and len(path) > 0:
            return path
        
        # Condição de parada: chegamos ao final da lista sem atingir a soma
        if index == n:
            return None
            
        # Ramo 1: Incluir o elemento atual S[index] no subconjunto
        res = backtrack(index + 1, current_sum + S[index], path + [S[index]])
        if res is not None:
            return res
            
        # Ramo 2: Não incluir o elemento atual e avançar para o próximo
        res = backtrack(index + 1, current_sum, path)
        if res is not None:
            return res
            
        return None

    return backtrack(0, 0, [])

if __name__ == "__main__":
    print("="*50)
    print(" Problema da Soma de Subconjuntos (Subset Sum) ")
    print("="*50)
    print("Classe: NP-Completo")
    print("Complexidade de Tempo: O(2^n)\n")

    # Cenário 1: Tamanho Pequeno (n=4)
    S1 = [2, 4, 6, 10]
    T1 = 16
    print(f"--- Tamanho Pequeno (n={len(S1)}) ---")
    print(f"S = {S1}, Alvo T = {T1}")
    resultado1 = subset_sum_backtracking(S1, T1)
    print(f"Resultado: {resultado1}\n")

    # Cenário 2: Tamanho Médio (n=8)
    S2 = [-5, -2, 1, 3, 7, 12, 15, 21]
    T2 = 0
    print(f"--- Tamanho Médio (n={len(S2)}) ---")
    print(f"S = {S2}, Alvo T = {T2}")
    resultado2 = subset_sum_backtracking(S2, T2)
    print(f"Resultado: {resultado2}\n")

    # Cenário 3: Tamanho Grande (n=30)
    # Gerando 30 números inteiros aleatórios de 5 dígitos conforme exemplo da imagem
    random.seed(42) # Usando seed fixa para reprodutibilidade dos valores
    S3 = [random.randint(10000, 99999) for _ in range(30)]
    T3 = 500000 
    
    print(f"--- Tamanho Grande (n={len(S3)}) ---")
    print(f"S = {S3[:5]} ... [total de 30 elementos de 5 dígitos]")
    print(f"Alvo T = {T3}")
    print("Iniciando busca (pode explorar até ~1 bilhão de combinações no pior caso)...")
    
    inicio = time.time()
    
    # O backtracking pode encontrar rapidamente dependendo da ordem ou demorar bastante.
    # Em cenários reais com n=30, algoritmos como 'Meet-in-the-middle' com O(2^(n/2)) são preferíveis.
    resultado3 = subset_sum_backtracking(S3, T3)
    
    fim = time.time()
    if resultado3:
        print(f"Resultado Encontrado: {resultado3}")
        print(f"Soma de verificação: {sum(resultado3)}")
    else:
        print("Nenhum subconjunto encontrado que some exatamente o Alvo T.")
    print(f"Tempo de execução: {fim - inicio:.4f} segundos\n")
