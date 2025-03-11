import sqlite3

# Ruta y nombre de la Base de datos SQLite
rutaBD = r"D:\Mis documentos\ProyectoA\Python\ProyectoA_SQLite\bd_sqlite.db"
try:
    with sqlite3.connect(rutaBD) as conBD:
        print(f"Base de datos {rutaBD} creada correctamente.")
        
        cursorBD = conBD.cursor()
        
        # Creamos la tabla clientes
        sql = """CREATE TABLE IF NOT EXISTS clientes 
                (
                    dni varchar(20),
                    nombre varchar(15),
                    telefono varchar(20)
                );"""        
        cursorBD.execute(sql)
        conBD.commit()
        print("Tabla clientes creada correctamente")
        
        # Leemos el contenido del fichero clientes.csv y lo pasamos
        # a la base de datos, a la tabla clientes
        print("Leyendo contenido del fichero datos_clientes.txt...")
        ficheroCSV = open(r"D:\Mis documentos\ProyectoA\Python\ProyectoA_SQLite\datos_clientes.csv")
        lineasFichero = ficheroCSV.readlines()
        numLines = len(lineasFichero)
        for i in range(numLines - 1):
            # Obtenemos los datos del fichero de texto CSV (las columnas van separadas por tabulador)
            dni = str(lineasFichero[i + 1].split("\t")[0])
            nombre = lineasFichero[i + 1].split("\t")[1]
            telefono = lineasFichero[i + 1].split("\t")[2]
            registro = f"'{dni}', '{nombre}', '{telefono}'"
            # Guardamos los datos en un registro de la tabla Tabla2 de la BD SQLite
            cursorBD.execute(f"INSERT INTO clientes (dni, nombre, telefono) VALUES ({registro})")
            print(f"Insertado registro {i+1} de {numLines-1} correctamente")
        # Aplicamos los cambios en la BD
        conBD.commit()
        print (f"Se han insertado correctamente {str(i + 1)} registros en la tabla clientes")
        print("Mostrando registros de la tabla SQLite...")
        
        # Ejecutamos la consulta SQL de SELECT para mostrar los registros de la tabla clientes
        sql = "select * from clientes"
        cursorBD.execute(sql)
        resultadoSQL = cursorBD.fetchall()
        for i in range(len(resultadoSQL)):
            print (resultadoSQL[i])                
except sqlite3.OperationalError as e:
    print("Error al trabajar con la BD SQLite:", e)