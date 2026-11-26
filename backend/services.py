from models import Producto
from repository import ProductoRepository

class Inventario:
    def __init__(self,repo):
        if not isinstance(repo, ProductoRepository):
             raise ValueError("El repositorio debe ser una  instancia de Productorepositorio")
        self.repo = repo

    def agregar_producto(self,producto):                
        if not isinstance(producto, Producto):
            raise ValueError("el producto debe ser una instancia de producto")   
        return self.repo.guardar(producto) 

    def obtener_producto(self,id_producto):
         if not isinstance(id_producto, int) or isinstance(id_producto, bool) or id_producto <=0:
              raise ValueError("el id debe ser un numero entero positivo")
         producto = self.repo.obtener_por_id(id_producto)
         if producto is None:
              raise ValueError("El producto no existe")
         return producto

    def listar_productos(self):
         productos = self.repo.listar()
         return [p.to_dict() for p in productos]

    def vender_producto(self,id_producto, cantidad):
         producto = self.obtener_producto(id_producto)
         producto.vender(cantidad)
         self.repo.actualizar(producto)
         return producto

    def reponer_producto(self, id_producto, cantidad):
         producto = self.obtener_producto(id_producto)
         producto.reponer_stock(cantidad)
         self.repo.actualizar(producto)
         return producto

    def eliminar_producto(self,id_producto):
         self.obtener_producto(id_producto)
         eliminado = self.repo.obtener_por_id(id_producto)
         if not eliminado:
              raise ValueError("No se pudo eliminar el producto")
     

