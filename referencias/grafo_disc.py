from DISClib.ADT import graph as g
from DISClib.ADT import list as lt
from DISClib.DataStructures import edge as e
from DISClib.ADT import stack
from DISClib.Algorithms.Graphs import bellmanford as bf
from DISClib.Algorithms.Graphs import bfs
from DISClib.Algorithms.Graphs import cycles as c
from DISClib.Algorithms.Graphs import dfs
from DISClib.Algorithms.Graphs import dfo
from DISClib.Algorithms.Graphs import prim
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.ADT import queue as q

class grafo:
    def __init__(self, type='Undirected'):               # done
        if type == 'Directed':
            self.estructura = g.newGraph(size=10, directed=True)
        else:
            self.estructura = g.newGraph(size=10)

    def addNode_byValue(self, infoNodo):    #done
        infoNodo = str(infoNodo)
        if not g.containsVertex(self.estructura, infoNodo):
            self.estructura = g.insertVertex(self.estructura, infoNodo)

    def addEdge_byValue(self, infoNodo_1, infoNodo_2, weight=0): #done
        infoNodo_1 = str(infoNodo_1)
        infoNodo_2 = str(infoNodo_2)
        self.estructura = g.addEdge(self.estructura, infoNodo_1, infoNodo_2, weight)

    def deleteNode_byValue(self, infoNodo): #done
        infoNodo = str(infoNodo)
        self.estructura = g.removeVertex(self.estructura, infoNodo)

    def deleteEdge_byValue(self, infoNodo_1, infoNodo_2):
        #TODO
        pass

    def getEdgeValues(self):                #done
        lst = list()
        iter = lt.iterator(g.edges(self.estructura))
        aux = ()
        for i in iter:
            aux = (i['vertexA'],i['vertexB'],i['weight'])
            lst.append(aux)
        return lst            
    
    def getNodeValues(self):                #done
        lst = list()
        iter = lt.iterator(g.vertices(self.estructura))
        for i in iter:
            lst.append(i)
        return lst

    def isNodeValue(self, infoNodo):        #done
        infoNodo = str(infoNodo)
        return g.containsVertex(self.estructura, infoNodo)

    def findAdjacentNode(self, infoNodo):   #done
        infoNodo = str(infoNodo)
        lst = list()
        try:
            iter = lt.iterator(g.adjacents(self.estructura, infoNodo))
            for i in iter:
                lst.append(i)
        except:
            pass
        return lst
    
    def algorithms(self, algoritmo, infoNodo=None):
        if infoNodo != None:
            infoNodo = str(infoNodo)
        table = list()
        if algoritmo == 'Bellman-Ford':
            search = bf.BellmanFord(self.estructura, infoNodo)
            for i in self.getNodeValues():
                costo = bf.distTo(search, i)
                path = list()
                if bf.hasPathTo(search, i):
                    iter = lt.iterator(bf.pathTo(search, i))
                    for j in iter:
                        path.append((j['vertexA'], j['vertexB']))
                else:
                    costo = 'inf'    
                my_dict = {'node': i, 'cost': costo, 'path': path}
                table.append(my_dict)
                
        if algoritmo == 'BreadhtFirstSearch':
            search = bfs.BreadhtFisrtSearch(self.estructura, infoNodo)
            for i in self.getNodeValues():
                if bfs.hasPathTo(search, i):
                    table.append(i)
                
        if algoritmo == "DirectedCycle":
            search = c.DirectedCycle(self.estructura)
            if c.hasCycle(search):
                pathRta = c.cycle(search)
                while not stack.isEmpty(pathRta):
                    edge = stack.pop(pathRta)
                    table.append((edge['vertexA'], edge['vertexB']))
        
        if algoritmo == 'DepthFirstSearch':
            search = dfs.DepthFirstSearch(self.estructura, infoNodo)
            for i in self.getNodeValues():
                if dfs.hasPathTo(search, i):
                    table.append(i)
        
        if algoritmo == 'DepthFirstOrder':
            search = dfo.DepthFirstOrder(self.estructura)
            while not stack.isEmpty(search['reversepost']):
                top = stack.pop(search['reversepost'])
                table.append(top)
                
        if algoritmo == 'PrimMST':
            search = prim.PrimMST(self.estructura, infoNodo)
            weight = prim.weightMST(self.estructura, search)
            path = search['mst']
            while not q.isEmpty(path):
                edge = q.dequeue(path)
                table.append((edge['vertexA'], edge['vertexB']))
            return table, weight
        
        if algoritmo == 'KosarajuSCC':
            sc = scc.KosarajuSCC(self.estructura)
            elements = sc['idscc']['table']['elements']
            table = dict()
            for i in elements:
                if i['value'] != None:
                    try:
                        lista = table[i['value']]
                        lista.append(i['key'])
                        table[i['value']] = lista
                    except:
                        table[i['value']] = [i['key']]
        
        if algoritmo == 'Dijkstra':
            search = djk.Dijkstra(self.estructura, infoNodo)
            for i in self.getNodeValues():
                if djk.hasPathTo(search, i):
                    path = djk.pathTo(search, i)
                    aux = dict()
                    pathList = list()
                    while not stack.isEmpty(path):
                        edge = stack.pop(path)
                        pathList.append((edge['vertexA'], edge['vertexB']))
                    aux['node'] = i
                    aux['path'] = pathList
                    aux['cost'] = djk.distTo(search, i)
                    table.append(aux)            
        return table