"""
Crea la tabla de usuarios de la EPS

"""
import psycopg2

# Reemplace los datos de conexion con los datos tomados de su servidor
connection = psycopg2.connect(database="neondb", user="ProfeBill", password="O4oU5naNIuRe", host="ep-round-mountain-97326230.us-east-2.aws.neon.tech", port=5432)

# Todas las instrucciones se ejecutan a tavés de un cursor
cursor = connection.cursor()
cursor.execute("""
create table usuarios (
  cedula varchar( 20 )  NOT NULL,
  nombre text not null,
  apellido text not null,
  telefono varchar(20),
  correo text,
  direccion text not null,
  codigo_municipio varchar(40) not null,
  codigo_departamento varchar(40) NOT NULL
);  
               """)

# Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
# pero si necesitan commit() para hacer los cambios persistentes


connection.commit()

# Si queremos deshacer los cambios, se hace rollback() en lugar de commit()
# connection.rollback()

