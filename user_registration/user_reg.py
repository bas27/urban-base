class User:

    """
    Класс пользователя, содержащий атрибуты: логин и пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


if __name__ == '__main__':
    database = Database()
    user = User(input('username: '), input('password: '), input('password_confirm: '))
    database.add_user(user.username, user.password)
