"""
Crea la tabla de usuarios de la EPS

"""
import sys
import psycopg2

# Reemplace los datos de conexion con los datos tomados de su servidor
connection = psycopg2.connect(database="neondb", user="ProfeBill", password="O4oU5naNIuRe", host="ep-round-mountain-97326230.us-east-2.aws.neon.tech", port=5432)

cedula = "8888888"
nombre = "Jaime"

try:

  # Todas las instrucciones se ejecutan a tavés de un cursor
  cursor = connection.cursor()
  cursor.execute(f"""
  insert into usuarios (
    cedula,   nombre,  apellido,  telefono,  correo, direccion, codigo_municipio, codigo_departamento
  )
  values 
  (
    '{cedula}',  '{nombre}', 'Velasquez', 31031031031, 'william@correo.com', 'la calle', '05001', '05'
  );
                """)

  # Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
  # pero si necesitan commit() para hacer los cambios persistentes


  connection.commit()

  # Verificar que haya quedado creado

  cursor.execute(f"SELECT nombre from usuarios where cedula = '{cedula}' ")
  resultado = cursor.fetchone()

  print( f"Quedo registrado con el nombre {resultado}")

  if resultado[0] == nombre :
      print("Guardado OK")
  else:
      print("Error al guardar")

  # Si queremos deshacer los cambios, se hace rollback() en lugar de commit()
  # connection.rollback()

except  :
  print( "Ocurrió un error al guardar en la base de datos")
  print( sys.exception() )
  connection.rollback() 