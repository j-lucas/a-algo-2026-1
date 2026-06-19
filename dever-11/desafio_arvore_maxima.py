# Desafio da Árvore Geradora Máxima (Kruskal Modificado)
# Este arquivo contém a implementação utilizando a estrutura de dados DSU (Union-Find)
# fornecida nas instruções, com a modificação na ordenação para encontrar o caminho mais caro sem ciclos.

class Grafo:
    def __init__(self):
        pass

    def buscar_raiz(self, pai, i):
        # Path Compression: aponta direto para a raiz
        if pai[i] == i:
            return i
        pai[i] = self.buscar_raiz(pai, pai[i])
        return pai[i]

    def unir_redes(self, pai, rank, x, y):
        # Union by Rank: rede maior absorve a menor
        raiz_x = self.buscar_raiz(pai, x)
        raiz_y = self.buscar_raiz(pai, y)

        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def kruskal_maximo(self, num_vertices, arestas):
        """
        Encontra a Árvore Geradora Máxima (caminho mais caro sem ciclos).
        Arestas deve ser uma lista de tuplas/listas no formato: (u, v, peso)
        """
        arvore_maxima = []
        pai = []
        rank = []

        # Inicializa cada vértice como sua própria rede (subconjunto)
        for no in range(num_vertices):
            pai.append(no)
            rank.append(0)

        # MODIFICAÇÃO PRINCIPAL: Ordena as arestas por peso em ordem DECRESCENTE (reverse=True)
        # para garantir que as arestas mais caras sejam processadas primeiro.
        arestas.sort(key=lambda x: x[2], reverse=True)

        for u, v, peso in arestas:
            raiz_u = self.buscar_raiz(pai, u)
            raiz_v = self.buscar_raiz(pai, v)

            # Se as raízes forem diferentes, não forma ciclo. Adiciona à árvore.
            if raiz_u != raiz_v:
                arvore_maxima.append((u, v, peso))
                self.unir_redes(pai, rank, raiz_u, raiz_v)

        return arvore_maxima

# --- Exemplo de Uso Prático ---
if __name__ == "__main__":
    # Exemplo de teste: 5 vértices (0 a 4)
    # Lista de arestas: (nó_origem, nó_destino, peso)
    arestas_exemplo = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 4, 5),
        (3, 4, 1)
    ]
    
    grafo = Grafo()
    num_vertices = 5
    
    resultado = grafo.kruskal_maximo(num_vertices, arestas_exemplo)
    
    print("Arestas selecionadas para a Árvore Geradora Máxima:")
    custo_total = 0
    for u, v, peso in resultado:
        print(f"Aresta ({u} -> {v}) com peso: {peso}")
        custo_total += peso
        
    print(f"Custo total máximo: {custo_total}")
