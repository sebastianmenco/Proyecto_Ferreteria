from models import Producto

class Inventario:
    def __init__(self, producto):
        self.__productos = {}

    def agregar_producto(self,producto):                
        if not isinstance(producto, Producto):
            raise ValueError("el producto debe ser una instancia de producto")    
        if producto.id in self.__productos:
                raise ValueError("Ese ID ya existe, escoja otro")
        else:
            self.__productos[producto.id] = producto
              