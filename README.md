programas-IA-busca

Programas em Python para buscas de caminho, baseados em algoritmos clássicos de grafos (BFS, DFS e Dijkstra):

Explicação de cada arquivo: 

---------------------------------------------------------------------------------------------------------------------------------------------------------------

1. busca_dfs_bfs - Programa em Python simula a busca de caminhos entre cidades utilizando dois algoritmos clássicos de grafos: BFS (Busca em Largura) e DFS (Busca em Profundidade). Ele é aplicado a um grafo que representa cidades do interior de São Paulo e suas conexões com distâncias.

Descrição do funcionamento:

 1. Representação do Grafo

O grafo é um dicionário de listas, onde cada chave representa uma cidade, e cada valor é uma lista de tuplas, contendo cidades vizinhas e a distância (em quilômetros) até elas.

Exemplo:

---python
'campinas': [('paulínia', 20)]
---

Significa que Campinas está ligada a Paulínia por uma estrada de 20 km.

---

 2. Algoritmo BFS

A função -bfs(grafo, origem, destino)- realiza uma busca em largura, ideal para encontrar o caminho com o menor número de cidades intermediárias (não necessariamente a menor distância). Ela usa uma fila (-deque-) para explorar os caminhos possíveis de forma iterativa, nível por nível.

---

 3. Algoritmo DFS

A função -dfs(grafo, origem, destino)- realiza uma busca em profundidade, utilizando recursão para explorar cada caminho até o fim antes de voltar e tentar outro. Pode encontrar caminhos rapidamente, mas nem sempre o mais curto.

---

 4. Cálculo da distância

A função -calcular_distancia(grafo, caminho)- percorre o caminho encontrado (lista de cidades) e soma todas as distâncias entre os pares de cidades consecutivas.

---

 5. Interação com o usuário (função -main-)

 Solicita ao usuário a cidade de origem, destino e o algoritmo de busca desejado (BFS ou DFS).
 Verifica se as cidades existem no grafo.
 Executa o algoritmo escolhido.
 Exibe o caminho encontrado e a distância total.
 Se não houver caminho possível, informa o usuário.

---

Exemplo de uso:

Se o usuário digitar:

---
Digite a cidade de origem: campinas
Digite a cidade de destino: piracicaba
Escolha o algoritmo de busca (BFS/DFS): bfs
---

O programa retornará:

---
Caminho escolhido: Campinas -> Paulínia -> Americana -> Piracicaba
Distância total: 61 km
---

Finalidade:

Esse programa pode ser usado como ferramenta educacional para estudar algoritmos de grafos (como foi inicialmente feito) ou como uma base para sistemas mais complexos, como rotas de navegação em mapas.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

2. mapa_cliente_dijkstra.py - Esse programa em Python implementa o algoritmo de Dijkstra para encontrar o caminho mais curto entre dois pontos em um grafo ponderado, representando um mapa de ruas.

---

Resumo do Funcionamento:

1. Criação do grafo: O grafo é construído com vértices e arestas, onde cada aresta tem um peso (distância).
2. Algoritmo de Dijkstra: Utiliza uma fila de prioridade (-heapq-) para processar os vértices com base na menor distância acumulada.
3. Entrada do usuário: O usuário informa o ponto de partida e o de chegada.
4. Cálculo do caminho: O programa calcula a menor distância entre os pontos usando Dijkstra e exibe o caminho percorrido.
5. Saída: Informa a distância mínima e o trajeto (ex: -A -> P1 -> D -> G -> Loja-).

---

Componentes principais

Classe -Graph-:

   Armazena os vértices e suas conexões.
   Método -add_edge()-: adiciona arestas ao grafo.
   Método -dijkstra()-: calcula a menor distância a partir de um ponto inicial.

Função -reconstruct_path()-:

   Reconstrói o trajeto do destino até a origem usando os dados do caminho mais curto.

---

Exemplo de uso

---plaintext
Digite o ponto de partida: A
Digite o ponto de chegada: K

A distância mínima de A até K é: 48 km
Caminho percorrido: A -> P1 -> D -> G -> Loja -> L -> K
---
----------------------------------------------------------------------------------------------------------------------------------------------------------------
