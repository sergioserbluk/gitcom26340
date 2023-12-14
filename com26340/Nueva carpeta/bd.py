import mysql.connector

# Configurar los detalles de la conexión
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'carritophp',
    'raise_on_warnings': True
}

# Intentar establecer la conexión
try:
    # Conectar a la base de datos MySQL
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        print('Conexión exitosa a la base de datos MySQL')

        # Realizar operaciones en la base de datos aquí
        # Crear un objeto Cursor para ejecutar consultas SQL
        cursor = conn.cursor()

        # Ejemplo de consulta
        cursor.execute('SELECT *  from usuarios')

        # Obtener los resultados de la consulta
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Cerrar el cursor
        cursor.close()
        conn.close

except mysql.connector.Error as err:
    print(f'Error: {err}')



# comando para instalar el conector de mysql en python
# pip install mysql-connector-python