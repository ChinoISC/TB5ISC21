import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='pruebabd'
    )

    cursor = connection.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Conectado a la base de datos MySQL. Versión: ", data)

except pymysql.MySQLError as e:
    print("Error al conectar a MySQL", e)

finally:
    connection.close()
    print("La conexión MySQL está cerrada")
