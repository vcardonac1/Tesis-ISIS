import config
from DISClib.ADT import list as lt

def defaultfunction(id1, id2):
    if type(id1) != type(id2):
        id1 = str(id1)
        id2 = str(id2)
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0

class listaEnlazada():
    def __init__(self, type):
        self.type = type
        if type == 1: 
            self.estructura = lt.newList(datastructure='SINGLE_LINKED', cmpfunction=defaultfunction)
        elif type == 2:
            self.estructura = lt.newList(datastructure='DOUBLE_LINKED', cmpfunction=defaultfunction)
    
    def addNode_byValue(self, infoNodo):
        lt.addLast(self.estructura, infoNodo)
    
    def deleteNode_byValue(self, infoNodo):
        pos = lt.isPresent(self.estructura, infoNodo)
        if pos > 1:
            lt.deleteElement(self.estructura, pos)
            return True
        elif pos == 1:
            lt.removeFirst(self.estructura)
            return True
        else:
            return False
    
    def getNodeValues(self):
        lst = list()
        iter = lt.iterator(self.estructura)
        for i in iter:
            lst.append(i)
        return lst
    
    def isNodeValue(self, infoNodo):
        if lt.isPresent(self.estructura, infoNodo) != 0:
            return True
        else:
            return False
    
    def findAdjacentNode(self, infoNodo):
        lst = list()
        pos = lt.isPresent(self.estructura, infoNodo)
        size = lt.size(self.estructura)
        if pos > 0:
            if self.type == 2 and pos-1 > 0:
                lst.append(lt.getElement(self.estructura, pos-1))
            if pos+1 <= size:
                lst.append(lt.getElement(self.estructura, pos+1))
        return lst
