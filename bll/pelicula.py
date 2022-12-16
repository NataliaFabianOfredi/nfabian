from dal.db import Db

def agregar(nombre, clasid, genero,precio, estado):    
    sql = "INSERT INTO PELICULAS (NOMBRE, CLASID, GENERO,PRECIO,ESTADO) VALUES(?, ?, ?, ?;?);"
    parametros = (nombre, clasid, genero, precio, estado)
    Db.ejecutar(sql, parametros)

def actualizar(nombre, clasid, genero, precio):    
    sql = "UPDATE PELICULAS SET NOMBRE = ?, CLASID = ?, GENERO = ?, PRECIO = ? WHERE PID = ? AND ESTADO = 1;"#may ESTADO SOLO BAJA LOGICA
    parametros = (nombre, clasid, genero, precio)#id
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:sql = "UPDATE PELICULAS SET ESTADO = 0 WHERE PID = ? AND ESTADO = 1;"
    else:
        sql = "DELETE FROM PELICULAS WHERE PID = ?;"
    parametros = (id)# parametros
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT p.PID, p.NOMBRE ,c.IDENTIFICACION, p.GENERO, p.PRECIO
            FROM PELICULAS p
            INNER JOIN CLASIFICACION c ON p.CLASID = c.CLASID
            WHERE p.ESTADO = 1;'''
    result = Db.consultar(sql)
    return result

def filtrar(pelicula):    #PARA RESERVA
    sql = '''SELECT p.NOMBRE, c.IDENTIDICACION, p.GENERO, p.PRECIO
            FROM PELICULAS p
            INNER JOIN CLASIFICACION c ON p.CLASID = c.CLASID
            WHERE p.PERSONAS LIKE ? AND p.ESTADO = 1;'''    
    parametros = ('%{}%'.format(pelicula),)    
    result = Db.consultar(sql, parametros)
    return result


def existe(pelicula):
    sql = "SELECT COUNT(*) FROM PELICULAS WHERE pelicula = ? AND Activo = 1;"
    parametros = (pelicula,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def obtener_id(id):
    sql = '''SELECT p.PID, p.NOMBRE, c.IDENTIFICACION Clasificacion, p.GENERO, p.PRECIO
            FROM PELICULAS p
            INNER JOIN CLASIFICACION c ON c.CLASID = p.CLASID
            WHERE p.PID = ? AND p.ESTADO = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

# def obtener_nombre_usuario(usuario):
#     sql = '''SELECT p.PID, p.NOMBRE, c.IDENTIFICACION Clasificacion, p.GENERO, p.PRECIO
#             FROM PELICULAS p
#             INNER JOIN CLASIFICACION c ON c.RolId = r.RolId
#             WHERE u.Usuario = ? AND u.Activo = 1;'''
#     parametros = (usuario,)
#     result = Db.consultar(sql, parametros, False)    
#     return result
# Footer
# © 2022 GitHub, Inc.
# Footer navigation
# Terms
# Privacy
# Security
# Status
# Docs
# Contact GitHub
# Pricing
# API
# Training
# Blog
# About
