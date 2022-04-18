import sqlite3


class Sqlite():
    """
    Clase para gestionar el trabajo con la base de datos sqlite.
    - Conectarse a la BD
    - Insertar
    - Actualizar
    - Borrar
    - Seleccionar
    """

    def __init__(self,bd) -> None:
        """
        Inicializa la clase con la propiedad nombre de la bd
        """
        self.__base_datos = bd


    def conectar(self):
        """
        Conecta/desconecta el codigo con la base de datos
        """
        cnx= sqlite3.connect(self.__base_datos)
        return cnx

    

    def seleccionar(self, consulta):

        cnx= self.conectar()
        cursor = cnx.cursor()
        cursor = cnx.execute(consulta)
        salida = cursor.fetchall()
        return salida

    def borrar(self,tabla,campo_id, valor_id):
        """
        Ejecuta la consulta de borrado de datos y devuelve el resultado
        """
        consulta=f'delete from {tabla} where {campo_id} = {valor_id};'
        cnx= self.conectar()
        cnx.execute(consulta)
        cnx.commit()
        cnx.close()


    def insertar(self):
        pass
    
    
    def actualizar(self):
        pass