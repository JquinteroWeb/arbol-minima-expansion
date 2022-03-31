import matplotlib.pyplot as plt
import networkx as nx

maquinas  = [[1,5,7],
             [2,3,4,7,8,9],
             [2,3,4,5,7,8,9,10],
             [6,7,8,9,10],
             [2,5,7,8,9,10],
             [1,2,3,7,8],
             [2,5,9],
             [3,4,7,9,10],
             [1,7,9,10],
             [7,8,9,10]];
             
def prim(G, s):# s es el nodo inicial para iniciar el algoritmo
    dist = {}   # dist registra la distancia mínima al nodo
    parent = {} # padre registra la tabla padre del árbol de expansión mínimo
    Q = list(G.nodes()) # Q contiene todos los nodos no cubiertos por el árbol de expansión
    MAXDIST = float('Inf') # MAXDIST significa infinito positivo, es decir, dos nodos no son adyacentes
    # Datos de inicialización
    # La distancia mínima de todos los nodos se establece en MAXDIST y el nodo principal se establece en Ninguno
    for v in G.nodes():
        dist[v] = MAXDIST
        #parent[v] = None
    # La distancia al nodo inicial s se establece en 0
    dist[s] = 0

    # Siga sacando el nodo "más cercano" de Q y agregándolo al árbol de expansión mínimo
    # Detiene el ciclo cuando Q está vacío, el algoritmo termina
    while Q:
        # Saque el nodo "más cercano" u y agregue u al árbol de expansión mínimo
        u = Q[0]
        for v in Q:
            if (dist[v] < dist[u]):
                u = v
        Q.remove(u)

        # Actualiza la distancia mínima de los nodos adyacentes de u
        for v in G.adj[u]:
            if (v in Q) and (G[u][v]['weight'] < dist[v]):
                parent[v] = u
                dist[v] = G[u][v]['weight']
                
    # El algoritmo finaliza y devuelve el árbol de expansión mínimo en forma de tabla principal
    return parent

def draw(g):
    pos = nx.spring_layout(g)
    nx.draw(g, pos, \
            arrows=True, \
            with_labels=True, \
            nodelist=g.nodes(), \
            style='solid', \
            edge_color='k', \
            width=1.5, \
            node_color='y', \
            alpha=0.85,
            )
    plt.show()
# autor:Juan Pablo Quintero Cataño
def matrizPesos(maquinas):
    pesos=[]
    for i in range(0,len(maquinas)):  

            maquina1=(maquinas[i])
            for k in range(i+1,len(maquinas)): 
                n = 0
                m = 0 
                maquina2=(maquinas[k])                       
                for j in range(0,len(maquina1)):          
                    for m in range(0,len(maquina2)):
                        
                        if(maquina1[j] == maquina2[m]):
                            n = n + 1
                m = (len(maquina1)-n) + (len(maquina2)-n)                
                
                # if (n==0):
                #     min = i+1
                #     max = k+1
                #     peso = (1-((n)/(n+m)))
                #     pesos.append((min,max,peso))
                # else:
                peso = (1-((n)/(n+m)))
                min = i+1
                max = k+1               
                pesos.append((min,max,peso))        
    return pesos

g_data=matrizPesos(maquinas)
g = nx.Graph()
g.add_weighted_edges_from(g_data)
tree = prim(g,1)

mtg = nx.Graph()
mtg.add_edges_from(tree.items())
draw(g) # Red original
draw(mtg) # Árbol de mínima expansión
peso=0
for k in tree.keys():
    peso+=g[k][tree[k]]['weight']

print("El peso total es "+ str( peso))



            




