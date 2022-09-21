from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash


from pprint import pprint

DATABASE = 'artistspaintings'

class Painting:

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.user_id = data['user_id']
        if 'first_name' in data:
            self.first_name = data['first_name']
        if 'last_name' in data:
            self.last_name = data['last_name']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO paintings (title, description, price, user_id) VALUES (%(title)s,%(description)s,%(price)s,%(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT paintings.*, first_name from paintings JOIN users ON users.id = paintings.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        paintings = []
        for painting in results:
            paintings.append(cls(painting))
        return paintings

    # ! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM paintings JOIN users on users.id = paintings.user_id WHERE paintings.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        painting = Painting(result[0])
        return painting

    # ! UPDATE
    @classmethod
    def update(cls,data):
        query = "UPDATE paintings SET title = %(title)s, description = %(description)s,price = %(price)s, user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! DELETE
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def get_painting_with_users(cls, data):
    #     query = "SELECT * FROM paintings LEFT JOIN users ON paintings.user_id = users.id LEFT JOIN users ON paintings.user_id = users.id WHERE paintings.id = %(id)s;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     painting = cls(results[0])
    #     for row_from_db in results:
    #         user_data = {
    #             "id": row_from_db["users.id"],
    #             "first_name": row_from_db["first_name"],
    #             "last_name": row_from_db["last_name"],
    #             "email": row_from_db["email"],
    #             "password": row_from_db["password"],
    #             "created_at": row_from_db["users.created_at"],
    #             "updated_at": row_from_db["users.updated_at"]
    #         }
    #         if row_from_db['first_name']:
    #             painting.users.append(painting.User(user_data))
    #         return painting        