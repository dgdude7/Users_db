from logger_base import log
from Conexion import Conexion


class CursorPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    def __enter__(self):
        log.debug('Inicia el metodo __enter__')
        self.__conn = Conexion.obtener_conexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Se inicia metodo __exit__')
        if exc_val:
            self.__conn.rollback()
            log.error(f'Ocurrio una excepcion, se hizo rollback: {exc_type} {exc_val} {exc_tb}')
        else:
            self.__conn.commit()
            log.debug('Commit de la transaccion\n')
        self.__cursor.close()
        Conexion.liberar_conexion(self.__conn)


if __name__ == '__main__':
    with CursorPool() as cursor:
        cursor.execute('SELECT * FROM usuarios')
        log.debug(cursor.fetchall())
