class Producto():
    def __init__(self,id, nombre, categoria, precio, stock):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.__stock = stock

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,nuevo_precio):
        if not isinstance(nuevo_precio, (float, int)) or nuevo_precio <= 0:
            raise ValueError("error al poner el numero")
        self.__precio = nuevo_precio 
        
    @property
    def stock(self):
        return self.__stock

    def reponer_stock(self,cantidad):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad a reponer debe ser un numero positivo")
        self.__stock += cantidad

    def vender(self,cantidad_vendida):
        if not isinstance(cantidad_vendida, int) or cantidad_vendida <= 0:
            raise ValueError("La cantidad solicitada debe ser un numero mayor que 0")
        if self.__stock < cantidad_vendida:
            raise ValueError(f"No hay suficientes unidades del producto {self.nombre}, hay en total {self.__stock} Unidades")
        else:
            self.__stock -= cantidad_vendida

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

