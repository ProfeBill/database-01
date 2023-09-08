"""
Ejemplo basico de conexion a PostgreSQL desde Python

"""
import psycopg2

# Reemplace los datos de conexion con los datos tomados de su servidor
connection = psycopg2.connect(database="neondb", user="ProfeBill", password="O4oU5naNIuRe", host="ep-round-mountain-97326230.us-east-2.aws.neon.tech", port=5432)

# Todas las instrucciones se ejecutan a tavés de un cursor
cursor = connection.cursor()
cursor.execute("SELECT * from departamentos;")

# Si la instruccion retorna resultados, se accede a ellos con fetchone() o fetchall()  segun la necesidad
record = cursor.fetchall()

print("Resultados : ")

# El resultado de fetchall() es una lista de tuplas
print(record)