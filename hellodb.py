"""
Ejemplo basico de conexion a PostgreSQL desde Python

"""
import psycopg2

# Reemplace los datos de conexion con los datos tomados de su servidor
connection = psycopg2.connect(database="#######", user="########", password="########", host="########", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * from departamentos;")

# Fetch all rows from database
record = cursor.fetchall()

print("Resultados : ")
print(record)