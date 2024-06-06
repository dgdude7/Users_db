from logger_base import log
from CursorPool import CursorPool
from Usuario import Usuario


class UsuarioDAO:
    __SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    __INSERTAR = 'INSERT INTO usuarios (id_usuario, username, password) VALUES (%s, %s, %s)'
    __ACTUALIZAR = 'UPDATE usuarios SET username=%s, password=%s WHERE id_usuario=%s'
    __ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            log.debug('Empezando metodo seleccionar')
            cursor.execute(cls.__SELECCIONAR)
            personas = cursor.fetchall()
            usuarios = []
            for persona in personas:
                usuario = Usuario(persona[0], persona[1], persona[2])
                usuarios.append(usuario)
            log.debug('Se extrajo exitosamente la lista de usuarios')
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            log.debug('Empezando metodo insertar')
            valores = (usuario.id_usuario, usuario.username, usuario.password)
            cursor.execute(cls.__INSERTAR, valores)
            log.debug(f'Se ha insertado exitosamente el {usuario} a la base de datos')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario, id_usuario):
        with CursorPool() as cursor:
            log.debug('Empezando metodo actualizar')
            valores = (usuario.username, usuario.password, id_usuario)
            cursor.execute(cls.__ACTUALIZAR, valores)
            log.debug(f'Se ha actualizado exitosamente el Usuario: [{id_usuario}, {usuario.username}, {usuario.password}] a la base de datos')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, id_usuario):
        with CursorPool() as cursor:
            log.debug('Iniciando el metodo eliminar')
            valores = (id_usuario,)
            cursor.execute(cls.__ELIMINAR, valores)
            log.debug(f'Se ha eliminado correctamente el usuario con id: {id_usuario}')
            return cursor.rowcount


if __name__ == '__main__':
    '''
    # INSERTAR
    usuario = Usuario(2,'lotitupi','admin')
    usuarios_insertados = UsuarioDAO.insertar(usuario)
    log.debug(f'Usuarios insertados: {usuarios_insertados}')
    '''
    '''
    # ACTUALIZAR
    usuario = Usuario(username='dgdude', password='admin')
    UsuarioDAO.actualizar(usuario, 1)
    '''
    '''
    # Eliminar
    UsuarioDAO.eliminar(2)
    '''
    # SELECCIONAR
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
    print(usuarios)
