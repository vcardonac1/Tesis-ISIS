from DISClib.ADT import graph as g
from DISClib.ADT import list as lt
from DISClib.DataStructures import edge as e

class grafo:
    def __init__(self, type='Undirected'):               # done
        if type == 'Directed':
            self.estructura = g.newGraph(size=10, directed=True)
        else:
            self.estructura = g.newGraph(size=10)

    def addNode_byValue(self, infoNodo):    #done
        self.estructura = g.insertVertex(self.estructura, infoNodo)

    def addEdge_byValue(self, infoNodo_1, infoNodo_2, weight=0): #done
        self.estructura = g.addEdge(self.estructura, infoNodo_1, infoNodo_2, weight)

    def deleteNode_byValue(self, infoNodo): #done
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
        return g.containsVertex(self.estructura, infoNodo)

    def findAdjacentNode(self, infoNodo):   #done
        lst = list()
        iter = lt.iterator(g.adjacents(self.estructura, infoNodo))
        for i in iter:
            lst.append(i)
        return lst