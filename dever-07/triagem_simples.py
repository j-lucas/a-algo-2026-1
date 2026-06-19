import heapq

# Max-Heap: usamos dor negativa pois heapq é min-heap
fila = []  # elementos: (-dor, nome)

def inserir(nome, dor):
    heapq.heappush(fila, (-dor, nome))
    print(f"[+] {nome} inserido (dor={dor})")

def atender():
    if not fila:
        print("Fila vazia!")
        return
    dor, nome = heapq.heappop(fila)
    print(f"[✓] Atendendo: {nome} (dor={-dor})")

def ajustar_prioridade(nome, nova_dor):
    # Remove o paciente e reinsere com nova dor — O(N) busca + O(log N) inserção
    global fila
    fila = [p for p in fila if p[1] != nome]
    heapq.heapify(fila)
    inserir(nome, nova_dor)
    print(f"[~] Prioridade de {nome} atualizada para dor={nova_dor}")

def exibir():
    ordenada = sorted(fila, key=lambda x: x[0])  # menor neg = maior dor
    print("\n--- Fila de triagem ---")
    for i, (neg_dor, nome) in enumerate(ordenada, 1):
        print(f"  {i}. {nome} | dor={-neg_dor}")
    print("-----------------------\n")


# Teste
inserir("Maria",  7)
inserir("João",   3)
inserir("Ana",   10)
inserir("Pedro",  5)
inserir("Luísa",  8)

exibir()

ajustar_prioridade("João", 9)   # Increase Key
ajustar_prioridade("Ana",  4)   # Decrease Key

exibir()

print("Atendendo todos:")
while fila:
    atender()
