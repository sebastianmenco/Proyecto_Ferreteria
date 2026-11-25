from models import Producto 

producto1 = Producto(1,"Martillo" , "Herramienta" , 15000, 30)
producto1.reponer_stock(10)
#assert producto1.stock == 30, "el total de stock deberia ser 40" 

try:
    producto1.vender(50)
    assert False, "debio lanzar el ValueError por falta de stock"
except ValueError:
    print("no alcanza la cantidad de unidades para esa compra")