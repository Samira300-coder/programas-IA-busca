class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.graph = []  # Lista para armazenar as arestas

    # Adiciona uma aresta ao grafo
    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    # Função auxiliar para encontrar o subconjunto de um elemento i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Função auxiliar para unir dois subconjuntos
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Função para implementar o Algoritmo de Kruskal
    def kruskal(self):
        result = []  # Armazenar a árvore geradora mínima
        i, e = 0, 0  # Variáveis para contar as arestas
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Ordenar arestas por peso
        parent = []
        rank = []

        # Inicializar subconjuntos para cada vértice
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Número de arestas em uma árvore geradora mínima é V-1
        while e < self.V - 1:
            u, v, weight = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # Se incluir essa aresta não formar um ciclo, inclua na árvore
            if x != y:
                e += 1
                result.append([u, v, weight])
                self.union(parent, rank, x, y)

        # Exibir a árvore geradora mínima
        print("Arestas na árvore geradora mínima:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight} km")
        total_weight = sum([weight for _, _, weight in result])
        print(f"Peso total da árvore: {total_weight} km")


# Definindo o grafo do mapa
g = Graph(14)  # 14 cidades no mapa

# Adicionando as arestas entre as cidades (baseado no mapa)
g.add_edge(0, 1, 30)  # Piracicaba -- Americana
g.add_edge(1, 2, 22)  # Americana -- Paulínia
g.add_edge(2, 3, 23)  # Paulínia -- Monte Mor
g.add_edge(3, 4, 15)  # Monte Mor -- Campinas
# Adicionar as outras arestas conforme o mapa

# Executar o algoritmo de Kruskal
g.kruskal()
