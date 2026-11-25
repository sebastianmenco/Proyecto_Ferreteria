from models import Producto
from services import Inventario

inventario = Inventario()

p1 = Producto(1, "Martillo", "Herramienta", 15000, 30)
p2 = Producto(2, "Alicate", "Herramienta", 12000, 10)

# 1. Agregar y obtener
inventario.agregar_producto(p1)
inventario.agregar_producto(p2)

obtenido = inventario.obtener_producto(1)
assert obtenido.nombre == "Martillo"
assert obtenido.stock == 30

# 2. Listar
listado = inventario.listar_productos()
assert len(listado) == 2

# 3. ID duplicado -> debe lanzar ValueError
p1_duplicado = Producto(1, "Martillo Copado", "Herramienta", 16000, 5)
try:
    inventario.agregar_producto(p1_duplicado)
    assert False, "Debió lanzar ValueError por ID duplicado"
except ValueError:
    pass

# 4. Vender producto válido y luego vender de más -> ValueError
inventario.vender_producto(1, 5)
assert inventario.obtener_producto(1).stock == 25

try:
    inventario.vender_producto(1, 100)
    assert False, "Debió lanzar ValueError por falta de stock"
except ValueError:
    pass

# 5. Reponer producto válido y cantidad inválida -> ValueError
inventario.reponer_producto(2, 10)
assert inventario.obtener_producto(2).stock == 20

try:
    inventario.reponer_producto(2, 0)
    assert False, "Debió lanzar ValueError por cantidad inválida"
except ValueError:
    pass

# 6. Eliminar producto y verificar que ya no existe -> ValueError
inventario.eliminar_producto(2)
assert len(inventario.listar_productos()) == 1

try:
    inventario.obtener_producto(2)
    assert False, "Debió lanzar ValueError al buscar un producto eliminado"
except ValueError:
    pass

print("Todas las pruebas de Inventario pasaron.")