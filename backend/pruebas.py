from models import Producto 
from services import Inventario

producto1 = Producto(1,"Martillo" , "Herramienta" , 15000, 30)
producto2 = Producto(1, "Sierra", "Herramienta" , 20000, 10)
#producto1.reponer_stock(10)
#assert producto1.stock == 30, "el total de stock deberia ser 40" 

#try:
#    producto1.vender(50)
#    assert False, "debio lanzar el ValueError por falta de stock"
#except ValueError:
#    print("no alcanza la cantidad de unidades para esa compra")

inventario = Inventario()
inventario.agregar_producto(producto1)

encontrado = inventario.obtener_producto(1)
assert encontrado.nombre == "Martillo", "Debio ser martillo"
assert encontrado.stock == 30, "Debio ser 30" 

productos = inventario.listar_productos()
print("Listado actual" , productos)

try:
    inventario.agregar_producto(producto2)
    assert False, "Debio dar Value Error"
except ValueError:
    print("ese id ya existe ome")