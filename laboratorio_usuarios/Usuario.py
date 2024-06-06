class Usuario:
    def __init__(self, id_usuario=None, username='User', password='admin'):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__password = password

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        return f'Usuario: id {self.id_usuario}, username: {self.username}, password: {self.password}'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    usuario1 = Usuario(1, 'dgdude', 'admin')
    print(usuario1)
