from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash



from pprint import pprint

DATABASE = 'tvshows'

class Tvshow:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.network = data['network']
        self.date_made = data['date_made']
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
        query = "INSERT INTO tvshows (name, description, network, date_made, user_id) VALUES (%(name)s,%(description)s,%(network)s,%(date_made)s,%(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
        

    # ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT tvshows.*, first_name FROM tvshows JOIN users ON users.id = tvshows.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        tvshows = []
        for tvshow in results:
            tvshows.append(cls(tvshow))
        return tvshows

    # ! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM tvshows JOIN users on users.id=tvshows.user_id WHERE tvshows.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        tvshow = Tvshow(result[0])
        return tvshow

    # ! UPDATE
    @classmethod
    def update(cls,data):
        query = "UPDATE tvshows SET name = %(name)s, description = %(description)s,network = %(network)s,date_made = %(date_made)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! DELETE
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM tvshows WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_tvshow(tvshow):
        is_valid = True
        if len(tvshow['name']) < 4:
            is_valid = False
            flash("Sorry, use at least 4 characters for the title")
        if len(tvshow['description']) < 4:
            is_valid = False
            flash("Sorry, use at least 4 characters for description")
        return is_valid


# @classmethod
# def get_tvshow_with_users(cls, data):
#     query = "SELECT * FROM tvshows LEFT JOIN favorites ON favorites.tvshow_id = tvshows.id LEFT JOIN users ON favorites.user_id = users.id WHERE tvshows.id = %(id)s;"
#     results = connectToMySQL('tvshows').query_db(query, data)
#     # results will be a list of tvshow objects with the user attached to each row.
#     tvshow = cls(results[0])
#     for row_from_db in results:
#         # Now we parse the tvshow data to make instances of tvshows ="keyword from-rainbow">and add them into our list.
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
#             tvshow.users.append(user.User(user_data))
#         return tvshow        