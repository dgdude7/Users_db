from logger_base import log
from Usuario import Usuario
from UsuarioDAO import UsuarioDAO


opcion = None
respuestas_validas = ['1', '2', '3', '4', '5']

while opcion != '5':
    opcion = input('''
    Opciones:
    1) Listar usuarios
    2) Agregar usuario
    3) Actualizar usuario
    4) Eliminar usuario
    5) Salir de las opciones
    Elija lo que quiere hacer: ''')

    if opcion == '1':
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            print(f'-{usuario}')
    elif opcion == '2':
        id = int(input('Inserte el id del usuario que quiere agregar: '))
        username = input('Inserte el username del usuario que quiere agregar: ')
        password = input('Inserte el password del usuario que quiere agregar: ')
        usuario = Usuario(id, username, password)
        UsuarioDAO.insertar(usuario)
        print(f'El {usuario}, se ha agregado correctamente a la base de datos')
    elif opcion == '3':
        id = int(input('Inserte el id del usuario que quiere actualizar: '))
        username = input('Inserte el nuevo username: ')
        password = input('Inserte el nuevo password: ')
        usuario = Usuario(username=username, password=password)
        UsuarioDAO.actualizar(usuario, id)
        print(f'El usuario con id: {id}, ha sido actualizado')
    elif opcion == '4':
        id = int(input('Inserte el id del usuario que quiere eliminar: '))
        UsuarioDAO.eliminar(id)
        print(f'El usuario con id: {id}, ha sido eliminado')
    elif opcion not in respuestas_validas:
        print('Por favor ingrese una opcion valida')
