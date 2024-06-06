from logger_base import log
from psycopg2 import pool


class Conexion:
    __DATABASE = 'laboratorio_usuarios'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.__pool == None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CON,
                    cls.__MAX_CON,
                    database=cls.__DATABASE,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls.__DB_PORT,
                    host=cls.__HOST)
                log.debug(f'Creacion del pool exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                log.error(f'Hubo un error en la creacion del pool de conexiones: {e}')
        else:
            return cls.__pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')


    @classmethod
    def cerrar_pool(cls):
        cls.obtener_pool().closeall()
        log.debug('Se ha cerrado el pool de conexiones')


if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)
    conexion2 = Conexion.obtener_conexion()
    Conexion.cerrar_pool()