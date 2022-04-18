import unittest
from sql import Sqlite
from settings import BD

class TestSqlite(unittest.TestCase):
    def test_existencia(self):
        mi_bd= Sqlite(BD)
        cnx= mi_bd.conectar()
        self.assertIsNotNone(cnx)

    # def test_seleccionar(self):
    #     mi_bd= Sqlite(BD)
    #     resultado = mi_bd.seleccionar()
    #     print(resultado)

    def test_seleccionar_articulos(self):
        mi_bd = Sqlite(BD)
        consulta= 'select * from articulos'
        resultado= mi_bd.seleccionar(consulta)
        self.assertIsNotNone(resultado)


    def test_borrado_articulo(self):
        mi_bd= Sqlite(BD)
        resultado= mi_bd.borrar('articulos','id',1)
        self.assertIsNone(resultado)