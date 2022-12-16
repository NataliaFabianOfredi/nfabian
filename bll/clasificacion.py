from dal.db import Db

def listar():
    sql = "SELECT CLASID, IDENTIFICACION, APTO, DESCRIPCION FROM CLASIFICACION ORDER BY CLASID;"
    result = Db.consultar(sql)
    return result