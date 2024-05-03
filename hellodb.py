"""
Ejemplo basico de conexion a PostgreSQL desde Python

"""
import psycopg2

# Do not expose your Neon credentials to the browser

PGHOST='ep-autumn-mountain-a5g8loeq.us-east-2.aws.neon.tech'
PGDATABASE='tarjeta_credito'
PGUSER='tarjeta_credito_owner'
PGPASSWORD='QK41LCqVlbGY'
PGPORT=5432

# Reemplace los datos de conexion con los datos tomados de su servidor
connection = psycopg2.connect(database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PGPORT)

# Todas las instrucciones se ejecutan a tavés de un cursor
cursor = connection.cursor()
cursor.execute("SELECT codigo_departamento, nombre_departamento from departamentos;")

# Si la instruccion retorna resultados, se accede a ellos con fetchone() o fetchall()  segun la necesidad
record = cursor.fetchall()
print("Resultados : ")

# El resultado de fetchall() es una lista de tuplas
print(record)