# Ambiente de apoyo al aprendizaje de estructuras de datos
## Guia de Instalación
1. Descargue el repositorio en su computador
2. Ingrese desde Visual Studio Code a la carpeta principal del proyecto
3. Instale todas las dependencias necesarias. Para esto, en la terminal ejecute el siguiente comando:
_pip install -r requirements.txt_
4. Ingrese al archivo _ComponenteVisual.ipynb_ y ejecute todas las celdas. Al final del notebook encontrará la interfaz visual.

## Guia de Uso
Una vez haya instalado correctamente todas las dependencias y ejecutado las celdas del archivo _ComponenteVisual.ipynb_ podrá inciar a hacer uso de la aplicación.
* Para iniciar, debe seleccionar una estructura de datos de su autoría, o seleccionar la que viene como referencia en la carpeta _./referencias/_
* Una vez cargada la estructura, podrá hacer uso de las funcionalidades de la aplicación. En la ejecución de cada actividad, resivirá alertas en caso de que el 
resultado no concuerde con el esperado.

## Contratos: Estructura de datos 
En esta sección encontrará los contratos (nomenclatura, input/output) que debe cumplir su implementación para que sea compatible con la aplicación

### Listas Enlazadas
* \_\_init\_\_(self, type)
* addNode_byValue(self, infoNodo)
* deleteNode_byValue(self, infoNodo)
* getNodeValues(self)
* isNodeValue(self, infoNodo)
* findAdjacentNode(self, infoNodo)
