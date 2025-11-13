from collections import deque

def criar_grafo():#Perin
    return {}  # dicionário de adjacência

def inserir_vertice(grafo, vertice):#Noah
    if vertice not in grafo:
        grafo[vertice] = []
        print(f"Vértice '{vertice}' adicionado.")
    else:
        print("Vértice já existe.")

def inserir_aresta(grafo, origem, destino):#Gustavo
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)
    grafo[origem].append(destino)
    print(f"Aresta '{origem} -> {destino}' adicionada.")

def exibir_grafo(grafo):#Gustavo
    print("\n--- GRAFO ---")
    for v, vizinhos in grafo.items():
        print(f"{v} -> {vizinhos}")
    print("----------------\n")



def bfs_menor_caminho(grafo, inicio, destino):#Gustavo
    fila = deque()
    fila.append((inicio, [inicio]))  # 1. Inserir estrutura com vértice inicial e caminho

    visitados = []                   # 2. Lista de visitados vazia

    while fila:                      # 3. Enquanto a fila não estiver vazia
        vertice, caminho = fila.popleft()  # a. Retirar o primeiro item da fila

        # b. verificar se o vértice é o destino
        if vertice == destino:
            return caminho  # i. Retornar o caminho caso seja

        if vertice not in visitados:
            visitados.append(vertice)  # c. Marcar vértice como visitado

            vizinhos = grafo.get(vertice, [])  # d. Obter os vizinhos

            for v in vizinhos:  # e. Para cada vizinho
                # i. Verificar se o vizinho não está na fila
                # ii. Verificar se o vizinho já não foi visitado
                ja_na_fila = any(v == item[0] for item in fila)
                if not ja_na_fila and v not in visitados:
                    # iii. Adicionar estrutura com vizinho e caminho atualizado
                    fila.append((v, caminho + [v]))

    return []  # 4. Retornar vazio (não há caminho)


def main():#Perin
    grafo = criar_grafo()

    while True:
        print("""
--- MENU ---
1 - Inserir Vértice
2 - Inserir Aresta
3 - Exibir Grafo
4 - Buscar Menor Caminho (BFS)
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
            destino = input("Vértice destino: ")

            if inicio not in grafo or destino not in grafo:
                print("Um dos vértices não foi encontrado!")
            else:
                caminho = bfs_menor_caminho(grafo, inicio, destino)
                if caminho:
                    print("Menor caminho encontrado:", caminho)
                else:
                    print("Não existe caminho entre os vértices informados.")

        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()