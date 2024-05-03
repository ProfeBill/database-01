"""
Ejemplo basico de conexion a PostgreSQL desde Python

"""
import psycopg2
import SecretConfig

# Reemplace los datos de conexion con los datos tomados de su servidor
connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, 
                              password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)

depto = input("Ingrese el nombre del departamento: ")

# Todas las instrucciones se ejecutan a tavés de un cursor
cursor = connection.cursor()
query = f"""select  codigo_municipio, nombre_municipio
from municipios
where 
codigo_municipio like '%001'
and codigo_departamento = 
( select codigo_departamento 
from departamentos 
where departamentos.nombre_departamento = '{depto}' )"""

# print(query)

cursor.execute(query)

# Si la instruccion retorna resultados, se accede a ellos con fetchone() o fetchall()  segun la necesidad
record = cursor.fetchone()
print( f"La capital de {depto} es {record[1]} ")
