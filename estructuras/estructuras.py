from abc import ABC, abstractmethod
from DISClib.ADT import list as lt


"""
    Funciones canonicas
"""
class structureInterface(ABC):
    @abstractmethod
    def __init__(self, type, comparefunction=None):
        """
        Crea una estructura de datos

        Args:
            type: Tipo de la estructura que se va a crear
            comparefunction: Funcion de comparacion
        Returns:
            Un nueva estructura vacía
        Raises:
            Exception
        """
        pass
    
    @abstractmethod
    def getInfo(self):
        """
        Se da la información general de la estrcutura

        Args:
            -
        Returns:
            Información general de la estructura. (tipo, #nodos, #enlaces)
        Raises:
            Exception
        """
        pass

    @abstractmethod
    def addNode_byValue(self, infoNodo):
        """
        Crea un nodo con la inforación que entra por parámetro.

        Si la estructura es una lista, añade el nodo al final de la lista,
        en los otros casos solo se crea el nodo

        Args:
            infoNodo: Información que se alamacena en un nodo
        Returns:
            -
        Raises:
            Exception
        """
        pass

    @abstractmethod
    def deleteNode_byValue(self, infoNodo):
        """
        Elimina el nodo que almacena la información que entra por parámetro

        Args:
            infoNodo: Información del nodo
        Returns:
            -
        Raises:
            Exception
        """
        pass

    @abstractmethod
    def getNodeValues(self):
        """
        Devuelve una lista con la información de todos los nodos de la estructura

        Args:
            -
        Returns:
            Lista con la información de todos los nodos
        Raises:
            Exception
        """
        pass

    @abstractmethod
    def getEdgeValues(self):
        """
        Devuelve una lista con la información de todas los enlaces de la estructura

        Args:
            -
        Returns:
            Lista de tuplas con la información de todos los enlaces de la estructura

            (infoNodo_origen, infoNodo_dentino, weight)
        Raises:
            Exception
        """
        pass

    @abstractmethod
    def isNodeValue(self, infoNodo):
        """
        Indica si un nodo pertenece a la estructura dado su valor

        Args:
            infoNodo: Información de un nodo
        Returns:
            True si el nodo pertenece a la estrcutura, False de lo contrario
        Raises:
            Exception
        """
        pass

    @abstractmethod
    def findAdjacentNode(self, infoNodo):  # orden?
        """
        Devuelve los nodos adyacentes a un nodo dada su información (aquellos a los que tiene conexion)

        Args:
            infoNodo: Información del nodo
        Returns:
            Lista con la información de los nodos adyacentes al nodo dado
        Raises:
            Exception
        """
        pass

class listaEnlazada(structureInterface):
    
    def __init__(self, type, comparefunction=None):
        """
        Crea una estructura de datos

        Args:
            type: tipo de la lista enlazada (1:sencilla, 2:doble)
            comparefunction: Funcion de comparacion
        Returns:
            Un nueva lista enlazada vacía
        Raises:
            Exception
        """
        self.tipo = type
        if type == 1: 
            s_type = 'SINGLE_LINKED'
        else: 
            s_type = 'DOUBLE_LINKED'
        self.estructura = lt.newList(datastructure = s_type, cmpfunction=comparefunction)

    def getInfo(self):
        """
        Se da la información general de la estrcutura

        Args:
            -
        Returns:
            Información general de la estructura. (tipo, #nodos, #enlaces)
        Raises:
            Exception
        """
        info = {'tipo':self.tipo,
                '#nodos':lt.size(self.estructura),
                }
        return info

    def addNode_byValue(self, infoNodo):
        """
        Crea un nodo con la inforación que entra por parámetro.

        Si la estructura es una lista, añade el nodo al final de la lista,
        en los otros casos solo se crea el nodo

        Args:
            infoNodo: Información que se alamacena en un nodo
        Returns:
            -
        Raises:
            Exception
        """
        lt.addLast(self.estructura, infoNodo)

    def deleteNode_byValue(self, infoNodo):
        """
        Elimina el nodo que almacena la información que entra por parámetro

        Args:
            infoNodo: Información del nodo
        Returns:
            True si se elimina el elemento, False de lo contrario
        Raises:
            Exception
        """
        pos = lt.isPresent(self.estructura, infoNodo)
        
        if pos == 1:
            lt.removeFirst(self.estructura)
            return True
        elif pos == lt.size(self.estructura):
            lt.removeLast(self.estructura)
            return True
        elif pos != 0:
            lt.deleteElement(self.estructura, pos)
            return True
        return False

    def getNodeValues(self):
        """
        Devuelve una lista con la información de todos los nodos de la estructura.
        
        La lista se retorna en el orden en el que se tienen las conexiones

        Args:
            -
        Returns:
            Lista con la información de todos los nodos en el orden de las conexiones
        Raises:
            Exception
        """
        nodes = list()
        iter = lt.iterator(self.estructura)
        for i in iter:
            nodes.append(i)
        return nodes

    def getEdgeValues(self):
        """
        Devuelve una lista con la información de todas los enlaces de la estructura

        Args:
            -
        Returns:
            Lista de tuplas con la información de todos los enlaces de la estructura

            (infoNodo_origen, infoNodo_dentino)
        Raises:
            Exception
        """
        edges = list()
        nodos = self.getNodeValues()
        '''
        if len(nodos) > 0:
            edges.append((sep_inicio,nodos[0]))
            if self.tipo == 2:
                edges.append((nodos[0],sep_inicio))
        if self.tipo == 1:
            for i in range(len(nodos)):
                if i+1 < len(nodos):
                    edges.append((nodos[i],nodos[i+1]))  
                else:
                    edges.append((nodos[i],sep_final))
        if self.tipo == 2:
            for i in range(len(nodos)):
                if i+1 < len(nodos):
                    edges.append((nodos[i],nodos[i+1]))
                    edges.append((nodos[i+1],nodos[i]))  
                else:
                    edges.append((nodos[i],sep_final))
                    edges.append((sep_final,nodos[i]))
        '''
        return edges          

    def isNodeValue(self, infoNodo):
        """
        Indica si un nodo pertenece a la estructura dado su valor

        Args:
            infoNodo: Información de un nodo
        Returns:
            True si el nodo pertenece a la estrcutura, False de lo contrario
        Raises:
            Exception
        """
        if lt.isPresent(self.estructura, infoNodo) == 0:
            return False
        else:
            return True

    def findAdjacentNode(self, infoNodo):
        """
        Devuelve los nodos adyacentes a un nodo dada su información (aquellos a los que tiene conexion)

        Args:
            infoNodo: Información del nodo
        Returns:
            Lista con la información de los nodos adyacentes al nodo dado
        Raises:
            Exception
        """
        listaAdj = list()
        pos = lt.isPresent(self.estructura, infoNodo)
        if pos < lt.size(self.estructura) and pos > 0:
            listaAdj.append(lt.getElement(self.estructura, pos+1))

        if self.tipo == 2 and pos-1 > 0:
            listaAdj.append(lt.getElement(self.estructura, pos-1))
            
        return listaAdj