class SQLiteDatabase:
    def connect(self):
        print('connecting to db')

    def get_users(self):
        print('get users with SQL')


class MongoDatabase:  # Пример использования утинной типизации и полиморфизма
    def connect(self):
        print('Connecting to database')

    def get_users(self):
        print('get users with nosql')


class Server:
    def get_users(self, db):
        db = SQLiteDatabase()
        db.connect()
        users = db.get_users()
        return users


def get_db_from_config():
    print('read config')
    return SQLiteDatabase()


if __name__ == '__main__':
    server = Server()
    server.get_users(MongoDatabase())
