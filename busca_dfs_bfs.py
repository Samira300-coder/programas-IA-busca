from collections import deque

# Representação do Grafo encontrado na cidade
grafo = {
    'campinas': [('paulínia', 20)],
    'paulínia': [('campinas', 20), ('americana', 23)],
    'americana': [('paulínia', 23), ('sumaré', 22), ('piracicaba', 18)],
    'sumaré': [('americana', 22), ('monte mor', 15)],
    'monte mor': [('sumaré', 15), ('indaiatuba', 22)],
    'indaiatuba': [('monte mor', 22), ('salto', 20)],
    'salto': [('indaiatuba', 20), ('itu', 25)],
    'itu': [('salto', 25), ('porto feliz', 12)],
    'porto feliz': [('itu', 12), ('tietê', 12)],
    'tietê': [('porto feliz', 12), ('capivari', 30)],
    'capivari': [('tietê', 30), ('piracicaba', 32)],
    'piracicaba': [('capivari', 32), ('americana', 18)],
    'boituva': [('tatuí', 17), ('porto feliz', 12)],
    'tatuí': [('boituva', 17)],
    'sorocaba': [('itu', 8), ('boituva', 23)]
}

# Função para fazer a busca em BFS
def bfs(grafo, origem, destino):
    fila = deque([[origem]])
    visitados = set()

    while fila:
        caminho = fila.popleft()
        cidade = caminho[-1]

        if cidade in visitados:
            continue

        for vizinho, distancia in grafo[cidade]:
            novo_caminho = list(caminho)
            novo_caminho.append(vizinho)
            fila.append(novo_caminho)

            if vizinho == destino:
                return novo_caminho

        visitados.add(cidade)
    
    return None

# Função para DFS
def dfs(grafo, origem, destino, caminho=None, visitados=None):
    if caminho is None:
        caminho = [origem]
    if visitados is None:
        visitados = set()

    visitados.add(origem)

    if origem == destino:
        return caminho

    for vizinho, _ in grafo[origem]:
        if vizinho not in visitados:
            novo_caminho = dfs(grafo, vizinho, destino, caminho + [vizinho], visitados)
            if novo_caminho:
                return novo_caminho

    return None

# Função para calcular a distância total
def calcular_distancia(grafo, caminho):
    distancia_total = 0
    for i in range(len(caminho) - 1):
        for vizinho, distancia in grafo[caminho[i]]:
            if vizinho == caminho[i + 1]:
                distancia_total += distancia
                break
    return distancia_total

# Função principal
def main():
    origem = input("Digite a cidade de origem: ").strip().lower()
    destino = input("Digite a cidade de destino: ").strip().lower()
    algoritmo = input("Escolha o algoritmo de busca (BFS/DFS): ").strip().upper()

    if origem not in grafo or destino not in grafo:
        print("Uma ou ambas as cidades não existem no grafo.")
        return

    if algoritmo == 'BFS':
        caminho = bfs(grafo, origem, destino)
    elif algoritmo == 'DFS':
        caminho = dfs(grafo, origem, destino)
    else:
        print("Algoritmo inválido!")
        return

    if caminho:
        distancia = calcular_distancia(grafo, caminho)
        print("Caminho escolhido:", " -> ".join(caminho).title())
        print("Distância total:", distancia, "km")
    else:
        print("Não foi possível encontrar um caminho entre as cidades especificadas.")

if __name__ == "__main__":
    main()
