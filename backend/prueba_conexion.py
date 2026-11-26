import os
import mysql.connector
from mysql.connector import Error

try:
    # 1. Intentamos abrir la puerta hacia MySQL
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=os.getenv("DB_PASSWORD", "Sebser_c314"),
        database="Ferreteria_db",
    )

    if conexion.is_connected():
        print("¡Conexión exitosa con MySQL!")
        cursor = conexion.cursor()

        # 2. Le pedimos que nos muestre las tablas de esa base de datos
        cursor.execute("SHOW TABLES;")
        tablas = cursor.fetchall()
        print("Tablas encontradas:", tablas)

        cursor.close()

except Error as e:
    print(f"Error al conectar con MySQL: {e}")

finally:
    # 3. cerramos la conexión
    if "conexion" in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada correctamente.")