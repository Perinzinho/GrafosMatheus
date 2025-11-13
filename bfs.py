from collections import deque

def criar_grafo():#Joaquim
    return {}, []  # dicionário de adjacência e lista de arestas (opcional)

def inserir_vertice(grafo, vertice):#Perin
    if vertice not in grafo:
        grafo[vertice] = []
        print(f"Vértice '{vertice}' adicionado.")
    else:
        print("Vértice já existe.")

def inserir_aresta(grafo, origem, destino):#Noah
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)
    grafo[origem].append(destino)
    print(f"Aresta '{origem} -> {destino}' adicionada.")

def exibir_grafo(grafo):
    print("\n--- GRAFO ---")
    for v, vizinhos in grafo.items():
        print(f"{v} -> {vizinhos}")
    print("----------------\n")

# -------------------------------
# BUSCA EM LARGURA (BFS)
# -------------------------------
def busca_em_largura(grafo, inicio):#Noah
    fila = deque()          # 1. Inserir o vértice inicial na fila
    fila.append(inicio)

    visitados = []          # 2. Iniciar a lista de visitados vazia

    while fila:             # 3. Enquanto a fila não estiver vazia
        vertice = fila.popleft()      # a. Retirar o primeiro vértice da fila

        if vertice not in visitados:
            visitados.append(vertice)  # b. Marcar vértice como visitado

            vizinhos = grafo.get(vertice, [])  # c. Obter os vizinhos do vértice

            for v in vizinhos:  # d. Para cada vizinho
                # i. Não está na fila
                # ii. Não foi visitado
                if v not in fila and v not in visitados:
                    fila.append(v)  # iii. Adicionar o vizinho na fila

    return visitados  # 4. Retornar Visitados


def main():#Joaquim
    grafo, arestas = criar_grafo()

    while True:
        print("""
--- MENU ---
1 - Inserir Vértice
2 - Inserir Aresta
3 - Exibir Grafo
4 - Busca em Largura (BFS)
0 - Sair
""")
        op = input("Escolha: ")

        if op == "1":
            v = input("Nome do vértice: ")
            inserir_vertice(grafo, v)

        elif op == "2":
            o = input("Origem: ")
            d = input("Destino: ")
            inserir_aresta(grafo, o, d)

        elif op == "3":
            exibir_grafo(grafo)

        elif op == "4":
            inicio = input("Vértice inicial: ")
            if inicio not in grafo:
                print("Vértice não encontrado!")
            else:
                resultado = busca_em_largura(grafo, inicio)
                print("Ordem de visita:", resultado)

        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()