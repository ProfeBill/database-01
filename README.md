# Usando PostgreSQL con Python

## Prerrequisitos

- Tome nota del nombre de los datos de conexión a su base de datos. en neon.tech los encontrará en el Dashboard
- En su proyecto, instale el paquete psycho2 con el siguiente comando:  

    pip install psycopg2-binary
  
## Conexión

Reemplace los datos de conexion con los datos tomados de su servidor

    connection = psycopg2.connect(database="#######", user="########", password="########", host="########", port=5432)


## Para saber más

* Documentación de psycopg2
https://www.psycopg.org/docs/

