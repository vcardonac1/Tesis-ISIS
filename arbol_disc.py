from DISClib.ADT import orderedmap as omap
from DISClib.ADT import list as lt
from DISClib.Algorithms.Trees import traversal as tr

class bst():
    def __init__(self):
        self.estructura = omap.newMap(omaptype = 'BST', comparefunction = defaultfunction)

    def addNode_byValue(self, infoNodo):    
        self.estructura = omap.put(self.estructura, infoNodo, infoNodo)

    def deleteNode_byValue(self, infoNodo):
        exists = omap.contains(self.estructura, infoNodo)
        self.estructura = omap.remove(self.estructura, infoNodo)
        exists2 = omap.contains(self.estructura, infoNodo)
        if (exists != exists2):
            return True
        else:
            return False

    def getNodeValues(self, order='Preorder'):  # Recorrido por Niveles
        lst = list()
        if not omap.isEmpty(self.estructura):
            if order == 'Inorder':
                iter = lt.iterator(tr.inorder(self.estructura))
            elif order == 'Preorder':
                iter = lt.iterator(tr.preorder(self.estructura))
            elif order == 'Postorder':
                iter = lt.iterator(tr.postorder(self.estructura))
            elif order == 'Por Niveles':
                iter = recorridoPoNiveles(self.estructura)
            for i in iter:
                lst.append(i)
        return lst

    def isNodeValue(self, infoNodo):
        return omap.contains(self.estructura, infoNodo)

    def findAdjacentNode(self, infoNodo):
        node = omap.get(self.estructura, infoNodo)
        lst = list()
        if node != None:
            left = node['left']
            if left != None:
                lst.append(left['value'])
            right = node['right']
            if right != None:
                lst.append(right['value'])
        return lst

    def getAltura(self):
        return omap.height(self.estructura)

def defaultfunction(id1, id2):
    if type(id1) != type(id2):
        id1 = str(id1)
        id2 = str(id2)
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0

def recorridoPoNiveles(bstTree):
    # TODO: 
    pass