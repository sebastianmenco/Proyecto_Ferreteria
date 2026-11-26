import os
import mysql.connector
from mysql.connector import Error
from models import Producto


class ProductoRepository:
    def __init__(
        self,
        host=None,
        port=None,
        user=None,
        password=None,
        database=None,
    ):
        self.host = host or os.getenv("DB_HOST", "127.0.0.1")
        self.port = int(port or os.getenv("DB_PORT", "3306"))
        self.user = user or os.getenv("DB_USER", "root")
        self.password = password or os.getenv("DB_PASSWORD", "")
        self.database = database or os.getenv("DB_NAME", "Ferreteria_db")

    def _conectar(self):
        return mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
        )

    def _fila_a_producto(self, fila):
        # Ajusta el orden si tu SELECT especifica columnas en otro orden
        id_prod, nombre, categoria, precio, stock = fila
        return Producto(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            stock=stock,
            id=id_prod,
        )

    def guardar(self, producto):
        sql = """
            INSERT INTO products (nombre, categoria, precio, stock)
            VALUES (%s, %s, %s, %s)
        """
        valores = (
            producto.nombre,
            producto.categoria,
            producto.precio,
            producto.stock,
        )
        conexion = None
        cursor = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute(sql, valores)
            conexion.commit()
            producto.id = cursor.lastrowid
            return producto
        except Error as e:
            if conexion is not None and conexion.is_connected():
                conexion.rollback()
            raise RuntimeError(f"Error al guardar el producto en MySQL: {e}") from e
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    def obtener_por_id(self, id_producto):
        sql = """
            SELECT id, nombre, categoria, precio, stock
            FROM products
            WHERE id = %s
        """
        conexion = None
        cursor = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute(sql, (id_producto,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return self._fila_a_producto(fila)
        except Error as e:
            raise RuntimeError(f"Error al consultar el producto por ID: {e}") from e
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    def listar(self):
        sql = """
            SELECT id, nombre, categoria, precio, stock
            FROM products
            ORDER BY id ASC
        """
        conexion = None
        cursor = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute(sql)
            filas = cursor.fetchall()
            return [self._fila_a_producto(fila) for fila in filas]
        except Error as e:
            raise RuntimeError(f"Error al listar productos: {e}") from e
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    def actualizar(self, producto):
        if producto.id is None:
            raise ValueError("No se puede actualizar un producto sin ID")

        sql = """
            UPDATE products
            SET nombre = %s, categoria = %s, precio = %s, stock = %s
            WHERE id = %s
        """
        valores = (
            producto.nombre,
            producto.categoria,
            producto.precio,
            producto.stock,
            producto.id,
        )
        conexion = None
        cursor = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute(sql, valores)
            conexion.commit()
            return cursor.rowcount > 0
        except Error as e:
            if conexion is not None and conexion.is_connected():
                conexion.rollback()
            raise RuntimeError(f"Error al actualizar el producto: {e}") from e
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    def eliminar(self, id_producto):
        sql = "DELETE FROM products WHERE id = %s"
        conexion = None
        cursor = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute(sql, (id_producto,))
            conexion.commit()
            return cursor.rowcount > 0
        except Error as e:
            if conexion is not None and conexion.is_connected():
                conexion.rollback()
            raise RuntimeError(f"Error al eliminar el producto: {e}") from e
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()