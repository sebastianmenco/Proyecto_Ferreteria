from models import Producto

class Inventario:
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self,producto):                
        if not isinstance(producto, Producto):
            raise ValueError("el producto debe ser un numero entero")    
        if producto.id in self.__productos:
            raise ValueError("Ese ID ya existe, escoja otro")
        else:
            self.__productos[producto.id] = producto

    def obtener_producto(self,id_producto):
         if not isinstance(id_producto, int):
              raise ValueError("el id debe ser una instancia de producto")
         if id_producto not in self.__productos:
              raise ValueError("El producto no existe")
         else:
              return self.__productos[id_producto]

    def listar_productos(self):
         return [p.to_dict() for p in self.__productos.values()]

    def vender_producto(self,id_producto, cantidad):
         producto = self.obtener_producto(id_producto)
         producto.vender(cantidad)

    def reponer_producto(self, id_producto, cantidad):
         producto = self.obtener_producto(id_producto)
         producto.reponer_stock(cantidad)

    def eliminar_producto(self,id_producto):
         self.obtener_producto(id_producto)
         del self.__productos[id_producto]
     

