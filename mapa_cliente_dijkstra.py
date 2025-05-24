""" 
Alunas: Isabela Neander Bassan
        Karine Melo Vieira e Silva
        Samira Rodrigues Pinheiro 

ADSMA6 - Programa 3 - Algoritmo de Dijkstra            30/09/2024
"""
# módulo heapq implementa uma fila de prioridade, 
# que é usada no algoritmo de Dijkstra para escolher o próximo vértice a ser processado 
# com base na menor distância conhecida.
import heapq

# Classe para representar o grafo. 
# self.vertices é um dicionário que contém todos os vértices do grafo como chaves. 
# Cada chave (um vértice) tem uma lista de tuplas associadas, 
# onde cada tupla contém um vértice vizinho e o peso (ou custo) da aresta que os conecta.

class Graph:
    def __init__(self):
        self.vertices = {}

    """
    Método para adicionar uma aresta ao grafo, conectando dois vértices com um determinado peso 
    (distância ou custo).

    - from_vertex: Vértice de origem.
    - to_vertex: Vértice de destino.
    - weight: O peso da aresta entre os dois vértices.
    
    Se o vértice de origem ou de destino ainda não existir no grafo, ele é adicionado. 
    A função garante que tanto o vértice de origem quanto o de destino existam no dicionário.
    """
    def add_edge(self, from_vertex, to_vertex, weight):

        # Se o vértice de origem não estiver no grafo, adiciona-o com uma lista vazia.

        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = []

        # Adiciona a conexão do vértice de origem para o vértice de destino, com o respectivo peso.

        self.vertices[from_vertex].append((to_vertex, weight))

        # Também adiciona o vértice de destino ao grafo, caso ele ainda não tenha sido adicionado.

        if to_vertex not in self.vertices:
            self.vertices[to_vertex] = []

    """
    Método que implementa o Algoritmo de Dijkstra para calcular o caminho mais curto a partir de um vértice inicial (start_vertex).
    
    - start_vertex: O vértice de partida.
    
    Retorna:
    - distances: Um dicionário contendo as menores distâncias conhecidas do vértice inicial até todos os outros vértices.
    - shortest_path_tree: Um dicionário que armazena o caminho percorrido (o vértice anterior para cada vértice no caminho mais curto).
    """
    def dijkstra(self, start_vertex):

        # Inicializa as distâncias com infinito para todos os vértices, exceto o de partida, que tem distância 0.
        
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0
        
        # A fila de prioridade começa com o vértice inicial e distância 0.
        
        priority_queue = [(0, start_vertex)]
        
        # O dicionário shortest_path_tree armazena o caminho mais curto.
        
        shortest_path_tree = {}

        # Processa a fila de prioridade até que todos os vértices tenham sido visitados.
        
        while priority_queue:

            # Remove e retorna o vértice com a menor distância da fila de prioridade.
            
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Se a distância atual for maior que a distância registrada, o vértice já foi processado.
            
            if current_distance > distances[current_vertex]:
                continue

            # Para cada vizinho (vértice conectado) do vértice atual, calcula a nova distância passando por ele.
            
            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight

                # Se a nova distância for menor que a distância registrada, atualiza as distâncias e o caminho mais curto.
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    shortest_path_tree[neighbor] = current_vertex

        # Retorna o dicionário de distâncias e o dicionário do caminho mais curto.
        
        return distances, shortest_path_tree


# Criando o grafo do mapa de ruas (grafo não-direcionado).

graph = Graph()

# Adicionando as arestas observadas no mapa com seus respectivos pesos (distâncias).
graph.add_edge('A', 'B', 10)
graph.add_edge('B', 'C', 13)
graph.add_edge('D', 'B', 6)
graph.add_edge('A', 'P1', 8)
graph.add_edge('P1', 'D', 7)
graph.add_edge('P1', 'E', 10)
graph.add_edge('D', 'G', 7)
graph.add_edge('G', 'D', 7)
graph.add_edge('G', 'Loja', 10)
graph.add_edge('Loja', 'K', 16)
graph.add_edge('Loja', 'L', 11)
graph.add_edge('L', 'K', 5)
graph.add_edge('E', 'F', 9)
graph.add_edge('G', 'F', 4)
graph.add_edge('F', 'H', 4)
graph.add_edge('E', 'I', 12)
graph.add_edge('I', 'J', 14)
graph.add_edge('J', 'K', 20)
graph.add_edge('H', 'J', 9)
graph.add_edge('J', 'H', 9)

"""
Função para reconstruir o caminho percorrido de trás para frente, começando do destino até o início.

- shortest_path_tree: O dicionário contendo o caminho mais curto.
- start: O vértice inicial.
- end: O vértice de destino.

Retorna:
- path: O caminho mais curto, na ordem correta (do ponto de partida ao destino).
"""
def reconstruct_path(shortest_path_tree, start, end):
    path = []
    current = end
    # Enquanto o vértice atual não for o inicial, adiciona o vértice ao caminho e segue para o anterior.
    while current != start:
        path.append(current)
        current = shortest_path_tree[current]
    # Adiciona o vértice inicial ao caminho.
    path.append(start)
    # Inverte a lista para que o caminho seja exibido na ordem correta.
    path.reverse()
    return path


# Solicita ao usuário os vértices de partida e destino
start_vertex = input("Digite o ponto de partida: ").strip()
destination_vertex = input("Digite o ponto de chegada: ").strip()

# Calcula a distância mínima usando o algoritmo de Dijkstra a partir do vértice inicial.
distances, shortest_path_tree = graph.dijkstra(start_vertex)

# Verifica se o destino está acessível.
if destination_vertex not in distances:
    print(f"O ponto de chegada '{destination_vertex}' não existe no grafo.")
else:
    # Verifica se há um caminho acessível. Caso contrário, a distância será infinita.
    if distances[destination_vertex] == float('infinity'):
        print(f"Não há caminho acessível de {start_vertex} até {destination_vertex}.")
    else:
        # Se há um caminho acessível, reconstrói o caminho percorrido e exibe a distância mínima.
        path_to_destination = reconstruct_path(shortest_path_tree, start_vertex, destination_vertex)
        print(f"A distância mínima de {start_vertex} até {destination_vertex} é: {distances[destination_vertex]} km")
        print(f"Caminho percorrido: {' -> '.join(path_to_destination)}")
